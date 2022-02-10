import asyncio


"""
ASYNCIO EVENT
"""


async def waiter(i: int, event: asyncio.Event) -> None:
    print(f"Waiter {i} waititng for event to happen")
    await event.wait()
    print(f"Waiter {i} is dont waiting")


async def main() -> None:
    event = asyncio.Event()
    waiter_tasks = [asyncio.create_task(waiter(i, event)) for i in range(5)]
    await asyncio.sleep(1.0)
    print("\nSetting event")
    event.set()
    await asyncio.gather(*waiter_tasks)
    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
