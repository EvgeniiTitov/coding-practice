import anyio
import random


"""
That will loop forever unless you use await tg.cancel_scope.cancel()
"""


async def loop_forever():
    try:
        while True:
            print("Looping")
            await anyio.sleep(random.random())
    except anyio.get_cancelled_exc_class():
        print("Looper cancelled, terminating")


async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(loop_forever)
        print("Looper started")
        await anyio.sleep(random.random())
        await tg.cancel_scope.cancel()
    print("Done")


if __name__ == "__main__":
    anyio.run(main)
