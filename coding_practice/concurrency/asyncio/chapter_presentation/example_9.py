import asyncio
import time
import io
from threading import Lock


'''
Running in threads
'''

stdout_lock = Lock()


def print_thread_safe(message: str) -> None:
    with stdout_lock:
        print(message)


def blocking_sleep() -> None:
    print_thread_safe(f"Block sleeping for {2} seconds")
    time.sleep(2.0)


def read_file_content(filepath: str, buffer: io.StringIO) -> None:
    print_thread_safe("Reading data from the file")
    with open(filepath, "r") as file:
        buffer.write(file.read())


def write_to_file(filepath: str, data: str) -> None:
    print_thread_safe("Writing data to a file")
    with open(filepath, "w") as file:
        file.write(data)


async def non_blocking_sleep() -> None:
    print_thread_safe(f"Non block sleeping for {2} seconds")
    await asyncio.sleep(2.0)


async def main() -> None:
    buffer = io.StringIO()
    coros = [
        asyncio.to_thread(blocking_sleep),
        asyncio.to_thread(
            read_file_content,
            "/Users/etitov1/Downloads/sample.txt", buffer
        ),
        asyncio.to_thread(
            write_to_file,
            "/Users/etitov1/Downloads/write_sample.txt", "Foo Bar"
        ),
        non_blocking_sleep()
    ]
    _ = await asyncio.gather(*coros, return_exceptions=True)

    buffer.seek(0)
    print(f"\nCoros finished. Buffer content: {buffer.getvalue()}")


if __name__ == '__main__':
    asyncio.run(main())
