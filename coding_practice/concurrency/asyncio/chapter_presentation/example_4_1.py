import asyncio
import random


'''
ASYNCIO GATHER 2

GATHER propagates the first encountered exception
'''


async def make_request(url: str) -> None:
    print(f"Making request to url: {url}")
    await asyncio.sleep(random.random())
    if "2" in url:
        raise Exception("Oops")


async def main() -> None:
    urls = (f"https://{i}.com" for i in range(5))
    request_coros = (make_request(url) for url in urls)
    try:
        results = await asyncio.gather(*request_coros)
    except Exception as e:
        print(f"Exception happened: {e}")
        raise


if __name__ == '__main__':
    asyncio.run(main())
