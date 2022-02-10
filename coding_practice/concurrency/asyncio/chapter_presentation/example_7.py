import asyncio

import aiohttp

"""
ASYNCIO WAIT

Returns 2 sets done and pending. Each contains tasks

FIRST_COMPLETED
FIRST_EXCEPTION
ALL_COMPLETED
"""


URLS = [
    "https://api.myip.com",
    "https://api.ipify.org?format=json",
    "https://api.my-ip.io/ip.txt",
]


async def make_request(session: aiohttp.ClientSession, url: str) -> tuple:
    print("Making request to:", url)
    response = await session.get(url)
    return url, await response.text()


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        request_tasks = [
            asyncio.create_task(make_request(session, url)) for url in URLS
        ]
        done, pending = await asyncio.wait(
            request_tasks, return_when=asyncio.FIRST_COMPLETED
        )
        print("Result:", done.pop().result())

        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        print("Pending tasks cancelled")
        assert all(task.cancelled() for task in pending)


if __name__ == "__main__":
    asyncio.run(main())
