import typing as t
import asyncio
import time
from functools import partial

from gcloud.aio.pubsub import (
    PublisherClient,
    PubsubMessage,
    SubscriberClient,
    SubscriberMessage,
)
import aiohttp


T = t.TypeVar("T")


async def make_request(url: str, session: aiohttp.ClientSession) -> str:
    response = await session.get(url)
    return await response.text()


async def _process_message(
    message: dict, session: aiohttp.ClientSession
) -> dict:
    name, index = message["name"], message["index"]
    requests_coro = asyncio.gather(
        *(
            make_request(f"https://api.agify.io?name={name}", session),
            make_request(f"https://api.genderize.io?name={name}", session),
            make_request(f"https://api.nationalize.io?name={name}", session),
        )
    )
    try:
        result = await asyncio.wait_for(requests_coro, timeout=2.0)
    except asyncio.TimeoutError:
        print(f"Processing of message {message} timed-out")
        raise
    except Exception as e:
        print(f"Failed processing message {message}. Error: {e}")
        raise
    return {
        "name": name,
        "index": index,
        "age": None,
        "gender": None,
        "nat": None,
    }


async def _get_batch(
    queue: asyncio.Queue[T],
    *,
    time_window: float = 3.0,
    max_items: t.Optional[int] = None,
) -> t.List[T]:
    batch: t.List[T] = []
    item = await queue.get()
    batch.append(item)
    while time_window > 0:
        if max_items and len(batch) == max_items:
            return batch
        start_time = time.perf_counter()
        try:
            item = asyncio.wait_for(queue.get(), timeout=time_window)
        except asyncio.TimeoutError:
            break
        else:
            batch.append(item)
            time_window -= time.perf_counter() - start_time
    return batch


def _mark_pending_items_as_complete(queue: asyncio.Queue[T]) -> None:
    items_count = 0
    while True:
        try:
            _ = queue.get_nowait()
        except asyncio.QueueEmpty:
            break
        items_count += 1
    for i in range(items_count):
        queue.task_done()


async def fetcher(
    subscription: str,
    queue: asyncio.Queue[SubscriberMessage],
    client: SubscriberClient,
    *,
    batch_size: int = 10,
    put_async: bool = False,
) -> None:
    """
    Fetches messages from a PubSub topic and puts them in the queue
    """
    try:
        while True:
            messages = await client.pull(subscription, batch_size, timeout=30)
            if not len(messages):
                continue
            for message in messages:
                if put_async:
                    asyncio.create_task(queue.put(message))
                else:
                    await queue.put(message)
    except asyncio.CancelledError:
        print("Fetcher cancelled. Terminated")


async def processor(
    in_queue: asyncio.Queue[SubscriberMessage],
    ack_queue: asyncio.Queue[str],
    out_queue: asyncio.Queue[t.Any],
    callback: t.Callable[[t.Any], t.Awaitable[t.Any]],
    max_concurrent_tasks: int,
) -> None:
    """
    Processes messages by getting a message from the in_queue, running the
    callback function against the message, then if successfull acking the
    message and putting the result in the out_queue
    """

    async def _execute_callback(message: bytes, message_id: str) -> None:
        # TODO: Convert message to dict here
        try:
            result = callback(message)
        except Exception as e:
            print(f"Failed to process message {message}. Error: {e}")
            return
        await asyncio.gather(ack_queue.put(message_id), out_queue.put(result))

    async def _consume_message(message: SubscriberMessage) -> None:
        msg_content, msg_id = message.data, message.ack_id
        await sema.acquire()
        task = asyncio.create_task(_execute_callback(msg_content, msg_id))
        task.add_done_callback(lambda f: sema.release())

    sema = asyncio.Semaphore(max_concurrent_tasks)
    try:
        while True:
            message = await in_queue.get()
            # TODO: Message validation could be done here (nack if not valid)
            await asyncio.shield(_consume_message(message))
            in_queue.task_done()
    except asyncio.CancelledError:
        print("Processor cancelled. Terminating gracefully")
        for i in range(max_concurrent_tasks):
            await sema.acquire()
        await ack_queue.join()
        print("Processor terminated gracefully")


async def acker(
    ack_queue: asyncio.Queue[str], client: SubscriberClient, subscription: str
) -> None:
    """Receives IDs of successfully processed messages and acks them"""
    try:
        while True:
            batch = await _get_batch(ack_queue, time_window=5.0)
            await client.acknowledge(subscription, batch)
            for _ in batch:
                ack_queue.task_done()
    except asyncio.CancelledError:
        print("Acker cancelled. Terminating gracefully")
        _mark_pending_items_as_complete(ack_queue)
        print("Acker terminated gracefully")


async def publisher(
    client: PublisherClient,
    topic: str,
    done_queue: asyncio.Queue[T],
    batch_size: int = 15,
) -> None:
    try:
        while True:
            batch = await _get_batch(done_queue, max_items=batch_size)
            batch = [PubsubMessage(str(item)) for item in batch]
            await client.publish(topic, messages=batch)
            for _ in batch:
                done_queue.task_done()
    except asyncio.CancelledError:
        print("Publisher cancelled. Terminating gracefully")
        _mark_pending_items_as_complete(done_queue)
        print("Publisher terminated gracefully")


async def main(subscription: str, topic: str) -> None:
    message_queue = asyncio.Queue()
    ack_queue = asyncio.Queue()
    done_queue = asyncio.Queue()
    tasks: t.List[asyncio.Task] = []
    async with aiohttp.ClientSession() as session:
        subscriber_client = SubscriberClient(session=session)
        publisher_client = PublisherClient(session=session)
        print("Queues, Clients and the Session created")
        tasks.append(
            asyncio.create_task(
                fetcher(subscription, message_queue, subscriber_client)
            )
        )
        tasks.append(
            asyncio.create_task(
                processor(
                    message_queue,
                    ack_queue,
                    done_queue,
                    partial(_process_message, session=session),
                    max_concurrent_tasks=50,
                )
            )
        )
        tasks.append(
            asyncio.create_task(
                acker(ack_queue, subscriber_client, subscription)
            )
        )
        tasks.append(
            asyncio.create_task(publisher(publisher_client, topic, done_queue))
        )
        print("Workers started")
        done, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


if __name__ == "__main__":
    subscription = ""
    topic = ""
    asyncio.run(main(subscription, topic), debug=True)
