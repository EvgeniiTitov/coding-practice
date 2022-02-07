import queue
import threading
from dataclasses import dataclass
import typing as t
from queue import Queue
import time


class Message:
    pass


@dataclass
class WorkItem(Message):
    name: str
    func: t.Callable[[t.Any], t.Any]
    args: t.Sequence[t.Any]
    kwargs: t.MutableMapping[str, t.Any]


class KillMessage(Message):
    pass


def do_something(a, b) -> tuple:
    if a == 5:
        raise Exception("Failed on 5")
    print(f"Thread {threading.get_ident()} processing {a} and {b}")
    time.sleep(1.0)
    return a, b


def worker(queue: Queue) -> None:
    while True:
        item = queue.get()
        if isinstance(item, KillMessage):
            print("Worker received kill message, stopping")
            queue.task_done()
            break
        func = item.func
        args = item.args
        kwargs = item.kwargs
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(
                f"Failed while running {func.__name__} with "
                f"args {args} and kwargs {kwargs}. Error: {e}"
            )
        else:
            print(
                f"Successfully ran {func.__name__} with args"
                f" {args}, kwargs {kwargs}. Result: {result}"
            )
        queue.task_done()


def producer(queue: Queue) -> None:
    for i in range(10):
        queue.put(
            WorkItem(
                name=str(i), func=do_something, args=(i,), kwargs=dict(b=i)
            )
        )
        print("Producer produced message:", i)
        time.sleep(0.5)
    queue.put(KillMessage())
    print("Kill message sent")


def main():
    channel = queue.Queue()
    worker_thread = threading.Thread(target=worker, args=(channel,))
    worker_thread.start()
    print("Worker started")

    print("Running producer")
    producer(channel)
    print("Producer stopped")

    channel.join()
    print("Queue joined")
    worker_thread.join()
    print("Worker joined")

    print("Main done")


if __name__ == "__main__":
    main()
