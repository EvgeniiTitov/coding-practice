import asyncio


"""
ASYNCIO SLEEP

asyncio.sleep() - for yielding control back to the event loop so that it can 
run something else. .sleep(0) for greedy functions 

queue of sleeping coros is priority based --> coros sleeping for 0 seconds will
be run straight away but the event loop will get a chance to do some house
keeping tasks (one cycle of event loop)
"""


async def worker() -> None:
    for i in range(7):
        print("Worker working...")
        await asyncio.sleep(1.0)


async def main() -> None:
    worker_task = asyncio.create_task(worker())
    for i in range(4):
        print("Main working...")
        await asyncio.sleep(1.0)
    await worker_task


if __name__ == "__main__":
    asyncio.run(main())
