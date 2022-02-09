import asyncio


'''
ASYNCIO WAIT_FOR

If timeout occurs, the task is cancelled.
'''

async def make_request(url: str) -> str:
    print(f"Making request to {url}")
    await asyncio.sleep(2.0)
    return "123"


async def main() -> None:
    task = asyncio.create_task(make_request("https://some_url.com"))
    try:
        response = await asyncio.wait_for(task, timeout=1.0)
    except asyncio.TimeoutError:
        print("Time out occured")
        print("Task cancelled?", task.cancelled())
    else:
        print(response)


if __name__ == '__main__':
    asyncio.run(main())
