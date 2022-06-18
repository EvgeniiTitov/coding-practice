import asyncio
from dataclasses import dataclass
import typing as t


class Message:
    pass


@dataclass(frozen=True)
class WorkItem(Message):
    name: str
    func: t.Callable[[], t.Awaitable[t.Any]]
    args: t.Sequence[t.Any]
    kwargs: t.MutableMapping[str, t.Any]


class KillMessage(Message):
    pass


async def do_something(a, b) -> tuple:
    if a == 5:
        raise Exception("Failed on 5")
    print(
        f"Asyncio Task {str(asyncio.tasks.current_task())[:42]} "
        f"processing {a} and {b}"
    )
    await asyncio.sleep(1.0)
    return a, b


async def worker(queue: asyncio.Queue) -> None:
    while True:
        item = await queue.get()
        if isinstance(item, KillMessage):
            print("Worker received kill message, stopping")
            queue.task_done()
            break
        func = item.func
        args = item.args
        kwargs = item.kwargs
        try:
            result = await func(*args, **kwargs)
        except Exception as e:
            print(
                f"FAILED while running {func.__name__} with "
                f"args {args} and kwargs {kwargs}. Error: {e}"
            )
        else:
            print(
                f"Successfully ran {func.__name__} with args"
                f" {args}, kwargs {kwargs}. Result: {result}"
            )
        queue.task_done()


async def producer(queue: asyncio.Queue) -> None:
    for i in range(10):
        await queue.put(
            WorkItem(
                name=str(i), func=do_something, args=(i,), kwargs=dict(b=i)
            )
        )
        print("Producer produced item:", i)
        await asyncio.sleep(0.3)
    await queue.put(KillMessage())
    print("Kill message sent")


async def main():
    queue = asyncio.Queue(maxsize=5)
    worker_task = asyncio.create_task(worker(queue))
    print("Worker task started")

    print("Running producer")
    await producer(queue)
    print("Producer stopped")

    await queue.join()
    print("Queue joined")

    # TODO: Could cancel and await it, instead we send kill message this time
    await worker_task
    print("Worker joined")

    print("Main done")


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
