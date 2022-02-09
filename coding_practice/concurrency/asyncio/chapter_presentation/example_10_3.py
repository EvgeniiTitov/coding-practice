import asyncio
import random

import aiohttp

"""
SEMAPHORE
"""

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=aud&ids=bitcoin"
TOTAL_TASKS = 10


async def _make_request(
        session: aiohttp.ClientSession, url: str, *args, **kwargs
) -> str:
    await asyncio.sleep(random.random())
    response = await session.get(url, *args, **kwargs)
    return await response.text()


async def make_request(
        i: int,
        sema: asyncio.Semaphore,
        session: aiohttp.ClientSession,
        url: str,
        *args, **kwargs
) -> str:
    async with sema:
        print(f"Making {i} request to {url}")
        return await _make_request(session, url, *args, **kwargs)


async def main() -> None:
    sema = asyncio.Semaphore(3)
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(make_request(i, sema, session, URL))
            for i in range(TOTAL_TASKS)
        ]
        gathered_tasks = asyncio.gather(*tasks, return_exceptions=True)
        try:
            results = await asyncio.wait_for(gathered_tasks, timeout=10.0)
        except asyncio.TimeoutError:
            print("Failed to complete all requests within timeout")
        else:
            print("\n\nResults:", results)


if __name__ == '__main__':
    asyncio.run(main())
