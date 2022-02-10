import asyncio
import random
from dataclasses import dataclass
import typing as t


"""
QUEUE + EVENT
"""


class BaseMessage:
    pass


class StopMessage(BaseMessage):
    pass


@dataclass
class WorkItem(BaseMessage):
    id: str
    data: str


async def fetcher(stop_event: asyncio.Event, queue: asyncio.Queue) -> None:
    def _new_item() -> t.Iterator[WorkItem]:
        i = 0
        while True:
            yield WorkItem(str(i), f"Data: {i}")
            i += 1

    item_generator = _new_item()
    while not stop_event.is_set():
        item = item_generator.__next__()
        print(f"Fetcher fetched item {item}")
        await queue.put(item)
        await asyncio.sleep(random.random())
    print("Fetcher stopping")
    await queue.put(StopMessage())
    await queue.join()
    print("Fetcher stopped")


async def processor(queue_in: asyncio.Queue, queue_out: asyncio.Queue) -> None:
    while True:
        item = await queue_in.get()
        queue_in.task_done()
        if isinstance(item, StopMessage):
            await queue_out.put(item)
            break
        print(f"Processor processed item {item}")
        await asyncio.sleep(random.random())
        await queue_out.put(item)
    await queue_out.join()
    print("Producer stopped")


async def publisher(queue: asyncio.Queue) -> None:
    while True:
        item = await queue.get()
        queue.task_done()
        if isinstance(item, StopMessage):
            break
        print(f"Publisher published the result")
        await asyncio.sleep(random.random())
    print("Publisher stopped")


async def main() -> None:
    message_queue = asyncio.Queue(20)
    result_queue = asyncio.Queue(20)
    stop_event = asyncio.Event()

    fetcher_task = asyncio.create_task(fetcher(stop_event, message_queue))
    processor_task = asyncio.create_task(
        processor(message_queue, result_queue)
    )
    publisher_task = asyncio.create_task(publisher(result_queue))
    print("Workers started")

    await asyncio.sleep(6)
    stop_event.set()
    await asyncio.gather(fetcher_task, processor_task, publisher_task)
    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
