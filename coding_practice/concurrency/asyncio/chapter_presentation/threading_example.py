from threading import Thread, get_ident, Lock
import os

from coding_practice.utils import timer


LOCK = Lock()


def safe_print(text):
    with LOCK:
        print(text)


def burn_cpu(i: int) -> None:
    safe_print(f"Burner {i}'s PID: {os.getpid()}; Thread: {get_ident()}")
    s = 0
    for i in range(100_000_000):
        s += i * i


@timer
def main() -> None:
    threads = [Thread(target=burn_cpu, args=(i,)) for i in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
