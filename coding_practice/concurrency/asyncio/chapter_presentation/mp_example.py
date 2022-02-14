from multiprocessing import Process
import threading
import os

from coding_practice.utils import timer


def burn_cpu(i: int) -> None:
    print(f"Burner {i}'s PID: {os.getpid()}; Thread: {threading.get_ident()}")
    s = 0
    for i in range(100_000_000):
        s += i * i


@timer
def main() -> None:
    processes = [Process(target=burn_cpu, args=(i,)) for i in range(5)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
