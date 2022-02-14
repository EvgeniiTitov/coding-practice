import asyncio


"""
Orphan tasks are easy to produce and hard to keep track of -> nurseries
"""


async def long_running_task() -> None:
    for i in range(30):
        print("Task running")
        await asyncio.sleep(1.0)


async def fire_and_forget() -> None:
    asyncio.create_task(long_running_task())
    print("Long running task started, returning")


async def main() -> None:
    await fire_and_forget()
    print("Main is ready to complete, yet the task is running")
    print(asyncio.all_tasks())
    await asyncio.sleep(5.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
