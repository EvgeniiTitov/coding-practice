import asyncio
import random

"""
AS COMPLETED

Return iterator of coros
"""


async def do_some_work(i):
    sleep = random.randint(0, 6)
    print(f"Doing work {i} for {sleep} seconds")
    await asyncio.sleep(sleep)
    return i


async def main() -> None:
    work_coros = [do_some_work(i) for i in range(10)]
    for coro in asyncio.as_completed(work_coros):
        result = await coro
        print(f"Work {result} is done")


if __name__ == "__main__":
    asyncio.run(main())
