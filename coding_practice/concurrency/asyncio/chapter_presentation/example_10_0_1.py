import asyncio


"""
Lock.locked()
"""

async def locker(lock: asyncio.Lock) -> None:
    async with lock:
        print("--> Locker locked the lock")
        await asyncio.sleep(10)
    print("--> Locker unlocked the lock")


async def main() -> None:
    lock = asyncio.Lock()
    locker_task = asyncio.create_task(locker(lock))
    print("Locker task created")

    print("Lock is locked?", lock.locked())
    await asyncio.sleep(1)
    print("Lock is locked?", lock.locked())

    print("Waiting for lock to unlock")
    while lock.locked():
        await asyncio.sleep(1.0)
    print("Must have unlocked by now? Locked:", lock.locked())

    await locker_task
    print("Done")



if __name__ == '__main__':
    asyncio.run(main())
