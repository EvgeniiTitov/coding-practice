import asyncio


"""
WRAPPING COROS INTO TASKS

Wrapping coros into tasks, so that they could be run concurrently
.ensure_future() = .create_task()
"""


async def say_after(delay: int, what: str) -> int:
    print(f"Sleeping {delay}. Word: {what}")
    await asyncio.sleep(delay)
    print(what)
    return delay


async def main() -> None:
    say_after_task_1 = asyncio.create_task(say_after(1, "Hello"))
    say_after_task_2 = asyncio.create_task(say_after(1, "World"))
    print("Tasks created")
    delay_1 = await say_after_task_1
    delay_2 = await say_after_task_2
    print(delay_1, delay_2)


if __name__ == "__main__":
    asyncio.run(main())
