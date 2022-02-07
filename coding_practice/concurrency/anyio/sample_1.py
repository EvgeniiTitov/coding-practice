import anyio
import asyncio
from dataclasses import dataclass
import random


'''
Is missing the two bad? I like nurseries
'''


@dataclass
class Message:
    index: int
    message: str


async def echo() -> None:
    i = 0
    try:
        while True:
            print(f"Echoing {i} ...")
            i += 1
            await asyncio.sleep(2.0)
    except asyncio.CancelledError:
        print("Echo cancelled, terminating")


async def producer(index: int, queue: asyncio.Queue) -> None:
    for i in range(10):
        message = Message(index, f"Message {i}")
        await queue.put(message)
        await asyncio.sleep(random.random())
        print(f"Producer {index} sent message {message}")


async def consumer(index: int, queue: asyncio.Queue) -> None:
    while True:
        item = await queue.get()
        print(f"Consumer {index} received message {item}")
        queue.task_done()
        await asyncio.sleep(random.random())


async def main() -> None:
    echo_task = asyncio.create_task(echo())
    print("Echo task started")

    queue = asyncio.Queue()

    # Nurseries are cool
    print("Creating a nursery")
    async with anyio.create_task_group() as tg:
        for i in range(2):
            tg.start_soon(producer, i, queue)
        print("Producers started, waiting for them to finish...")
    print("Producers done")

    consumer_tasks = [
        asyncio.create_task(consumer(index, queue)) for index in range(2)
    ]
    print("\nConsumers started, waiting for them to process all messages")
    await queue.join()
    print("Queue joined, all messages processed")

    print("All messages processed, cancelling the tasks ugly way")
    all_tasks = [echo_task, *consumer_tasks]
    for task in all_tasks:
        task.cancel()
    print("Tasks cancelled")

    # Return exception True is required to catch CancelledError exceptions
    # raised inside the concumers but never handled like its done in echo()
    _ = await asyncio.gather(*all_tasks, return_exceptions=True)
    print("All tasks terminated")


if __name__ == '__main__':
    anyio.run(main)
