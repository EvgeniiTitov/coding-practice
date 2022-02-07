import anyio
import random


"""
That will loop forever unless you use await tg.cancel_scope.cancel() 
"""


async def loop_forever():
    while True:
        print("Looping")
        await anyio.sleep(random.random())


async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(loop_forever)
        print("Looper started")
        await anyio.sleep(random.random())
        # await tg.cancel_scope.cancel()
    print("Done")


if __name__ == "__main__":
    anyio.run(main)
