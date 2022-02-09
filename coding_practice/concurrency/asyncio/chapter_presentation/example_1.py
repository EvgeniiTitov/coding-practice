import asyncio


'''
RUNNING COROS DIRECTLY

Sequential execution of coroutines -> await some_coro() blocks the logic, the
code does not go further until some_coro() completes.
'''


async def say_after(delay: int, what: str) -> int:
    await asyncio.sleep(delay)
    print(what)
    return delay


async def main() -> None:
    delay_1 = await say_after(1, "Hello")
    delay_2 = await say_after(1, "World")
    print(delay_1, delay_2)


if __name__ == '__main__':
    asyncio.run(main())
