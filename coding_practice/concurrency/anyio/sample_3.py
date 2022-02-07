import anyio
import random


async def consumer(index: int, receive_stream) -> None:
    async with receive_stream:
        async for message in receive_stream:
            print(f"Consumer {index} received message {message}")
            await anyio.sleep(random.random())


async def main():
    send_stream, receive_stream = anyio.create_memory_object_stream()
    print("Stream ends created")

    async with anyio.create_task_group() as tg:
        for i in range(2):
            tg.start_soon(consumer, i, receive_stream)
        print("Consumer started")

        async with send_stream:
            for i in range(10):
                await send_stream.send(f"Message: {i}")
                print(f"Message {i} created")
                await anyio.sleep(random.random())


if __name__ == "__main__":
    anyio.run(main)
