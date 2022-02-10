import asyncio
import signal
import typing as t


'''
ASYNCIO SIGNAL HANDLING
'''

async def worker() -> None:
    try:
        while True:
            print("Doing work...")
            await asyncio.sleep(1.0)
    except asyncio.CancelledError:
        print("Worker cancelled. Terminating...")


async def shutdown(
    sign: signal.Signals,
    loop: asyncio.AbstractEventLoop
) -> None:
    print(f"Shutdown callback called with signal {sign.name}. Cleaning up")
    # TODO: Close DB connections, nack pending messages etc

    tasks = [
        task for task in asyncio.all_tasks()
        if task is not asyncio.current_task()
    ]
    for task in tasks:
        task.cancel()
    print("Tasks cancelled. Awaiting their completion")
    _ = await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


def setup_signal_handlers(signals: t.Sequence[signal.Signals]) -> None:
    loop = asyncio.get_running_loop()
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(s, loop))
        )
    print("Signal handlers have been registered")


async def main() -> None:
    setup_signal_handlers((signal.SIGHUP, signal.SIGTERM, signal.SIGINT))
    await worker()
    print("Done")


if __name__ == '__main__':
    asyncio.run(main())
