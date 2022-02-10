import asyncio


"""
ASYNCIO LOCK
"""


async def worker(i: int, lock: asyncio.Lock) -> None:
    while True:
        async with lock:
            print(f"Worker {i} got the lock")
            await asyncio.sleep(0.5)


async def main() -> None:
    lock = asyncio.Lock()
    worker_tasks = [
        asyncio.create_task(worker(i, lock)) for i in range(5)
    ]
    print("Workers started")
    await asyncio.sleep(20)

    for task in worker_tasks:
        task.cancel()
    _ = await asyncio.gather(*worker_tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
