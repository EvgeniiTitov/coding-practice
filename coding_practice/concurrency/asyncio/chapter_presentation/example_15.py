import asyncio
import typing as t


async def consumer(event: asyncio.Event, queue: asyncio.Queue) -> None:
    while not event.is_set():
        item = await queue.get()
        print(f"Processing item: {item}")
        await asyncio.sleep(1.0)
    print("Worker done")


async def producer(event: asyncio.Event, queue: asyncio.Queue) -> None:
    def _task_generator() -> t.Iterator[str]:
        c = 0
        while True:
            yield f"Task {c}"
            c += 1
    gen = _task_generator()
    while not event.is_set():
        task = next(gen)
        await queue.put(task)
        print(f"{task} put in the queue")
        await asyncio.sleep(1.0)


async def main() -> None:
    event = asyncio.Event()
    queue = asyncio.Queue(10)
    producer_task = asyncio.create_task(producer(event, queue))
    consumer_task = asyncio.create_task(consumer(event, queue))
    await asyncio.sleep(5.0)
    event.set()
    await asyncio.gather(producer_task, consumer_task)
    print("Done")


if __name__ == '__main__':
    asyncio.run(main())

