import random
import anyio
import asyncio
import typing as t


"""
Nurseries make working with queue.join() painful?
"""


async def producer(index: int, queue: asyncio.Queue) -> None:
    i = 0
    try:
        while True:
            await queue.put(f"Message {index} {i}")
            print(f"Producer {index} create message {i}")
            i += 1
            await anyio.sleep(random.random())
    except anyio.get_cancelled_exc_class():
        print(f"Producer {index} cancelled")


async def consumer(index: int, queue: asyncio.Queue) -> None:
    try:
        while True:
            item = await queue.get()
            print(f"Consumer {index} received message {item}")
            queue.task_done()
            await anyio.sleep(random.random())
    except anyio.get_cancelled_exc_class():
        print("Consumer cancelled, terminating...")
        while True:
            try:
                _ = queue.get_nowait()
            except asyncio.queues.QueueEmpty:
                break
            else:
                queue.task_done()
    print("Consumer terminated")


async def main() -> None:
    queue: "asyncio.Queue[t.Any]" = asyncio.Queue(10)
    async with anyio.create_task_group() as tg:
        tg.start_soon(producer, 1, queue)
        tg.start_soon(producer, 2, queue)
        print("Producers started")

        tg.start_soon(consumer, 1, queue)
        print("Consumers started")

        await anyio.sleep(10)
        print("Cancelling workers")
        await tg.cancel_scope.cancel()

    await queue.join()
    print("Queue joined. Done")


if __name__ == "__main__":
    anyio.run(main)
