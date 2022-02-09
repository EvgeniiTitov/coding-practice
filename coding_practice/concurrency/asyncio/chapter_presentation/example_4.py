import asyncio

import aiohttp


'''
ASYNCIO GATHER 1
'''


URLS = [
    "https://api.agify.io?name={name}",
    "https://api.genderize.io?name={name}",
    "https://api.nationalize.io?name={name}"
]


async def make_request(session: aiohttp.ClientSession, url: str) -> str:
    print(f"Making request to {url}")
    response = await session.get(url)
    if "nationalize" in url:
        raise Exception("Oops")
    return await response.text()


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        request_coros = [
            make_request(session, url.format(name="Anton")) for url in URLS
        ]
        print("Coros created, awaiting their completion")

        results = await asyncio.gather(*request_coros, return_exceptions=True)

        for result in results:
            if isinstance(result, BaseException):
                print("Exception was raised in a coro:", result)
            else:
                print(result)


if __name__ == '__main__':
    asyncio.run(main())
