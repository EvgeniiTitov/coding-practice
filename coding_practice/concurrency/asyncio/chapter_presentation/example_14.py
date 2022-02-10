import asyncio
import random


"""
ASYNCIO EXCEPTION HANDLING


"""


async def broken_worker() -> None:
    while True:
        print("Broken worker working...")
        if random.random() > 0.2:
            raise Exception("WorkerFailed")


async def worker() -> None:
    while True:
        print("Worker busily working...")
        await asyncio.sleep(1.0)


async def monitor_worker_health(worker: asyncio.Task) -> None:
    while True:
        await asyncio.sleep(3.0)
        worker_name = worker.get_name()
        is_broken = worker.exception()
        print(f"Worker {worker_name} is broken {is_broken}")


async def main() -> None:
    loop = asyncio.get_running_loop()

    print("Got the loop:", loop)

    worker_task = asyncio.create_task(worker())
    broken_worker_task = asyncio.create_task(broken_worker(), name="broken")
    print("Workers started")

    monitor_task = asyncio.create_task(
        monitor_worker_health(broken_worker_task)
    )

    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
