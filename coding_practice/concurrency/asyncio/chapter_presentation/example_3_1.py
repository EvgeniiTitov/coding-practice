import asyncio


async def worker() -> None:
    try:
        while True:
            print("Worker working...")
            await asyncio.sleep(1.0)
    except asyncio.CancelledError:
        print("CancelError caught. Terminating...")
        # Could reraise or just return

async def main() -> None:
    worker_task = asyncio.create_task(worker())
    for i in range(4):
        print("Main working...")
        await asyncio.sleep(1.0)

    worker_task.cancel()
    await worker_task
    print("Worker cancelled")

if __name__ == "__main__":
    asyncio.run(main())

