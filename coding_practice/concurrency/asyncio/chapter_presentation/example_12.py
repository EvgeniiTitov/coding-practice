import asyncio
import random
import typing as t


"""
Task cancellation: catching vs not catching cancel errors
"""


async def message_fetcher(message_queue: asyncio.Queue) -> None:
    def _generate_new_message() -> t.Iterator[float]:
        counter = 1
        while True:
            yield counter
            counter += 1

    message_generator = _generate_new_message()
    while True:
        message = next(message_generator)
        print(f"Fetcher fetched message {message}")
        await message_queue.put(message)
        await asyncio.sleep(random.random())


async def message_consumer(message_queue: asyncio.Queue) -> None:
    try:
        while True:
            message = await message_queue.get()
            print(f"Consumer consumed message {message}")
            await asyncio.sleep(1.0)
    except asyncio.CancelledError:
        print("\nConsumer caught cancellation error. Terminating gracefully")
        while True:
            try:
                message = message_queue.get_nowait()
            except asyncio.QueueEmpty:
                break
            else:
                print(f"Gracefully handled pending message {message}")
        print("Consumer terminated gracefully\n")
        raise


async def stop_workers(workers: t.Sequence[asyncio.Task]) -> None:
    for worker in workers:
        worker.cancel()
    await asyncio.gather(*workers, return_exceptions=True)


async def main() -> None:
    message_queue = asyncio.Queue(10)
    fetcher_task = asyncio.create_task(message_fetcher(message_queue))
    consumer_task = asyncio.create_task(message_consumer(message_queue))
    print("Workers started")

    await asyncio.sleep(10)
    await stop_workers((fetcher_task, consumer_task))
    print("Workers stopped")


if __name__ == "__main__":
    asyncio.run(main())
