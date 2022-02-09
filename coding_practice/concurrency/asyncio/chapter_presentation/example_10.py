import asyncio
import threading
import time


'''
Synchronisation primitives:
- Locks
Asyncio one process, one thread. Used to run some expensive code once that
is requested by many

- Events
- Conditions
- Semaphores
- BoundedSemas
'''

LOCK = asyncio.Lock()


class _Token(threading.Thread):

    def __init__(self, valid_sec: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._valid_sec = valid_sec
        self._token = None

    @property
    def token(self) -> str:
        return self._token

    def set_token(self) -> None:
        "I am expensive call, don't make me often"
        print("Refreshing token...")
        time.sleep(3.0)
        self._token = "fmifo2hfnwe"
        print("Token refreshed")

    def run(self) -> None:
        while True:
            time.sleep(self._valid_sec)
            if self._token:
                self._token = None


class Token:

    def __init__(self, valid_sec: int) -> None:
        self._token_thread = _Token(valid_sec=valid_sec)
        self._token_thread.start()
        self._token_value = self._token_thread.token
        self._refresh_token = self._token_thread.set_token

    async def get_token(self) -> str:
        print("Token requested")
        async with LOCK:
            if self._token_value:
                print("Its already set, token returned")
                return self._token_value
            else:
                await asyncio.to_thread(self._refresh_token)
                return self._token_value


async def make_request(url: str, token: Token) -> None:
    token = await token.get_token()
    print(f"Making request to {url} with Bearer {token}")
    await asyncio.sleep(1.0)


async def main() -> None:
    token = Token(valid_sec=2)
    request_coros = [
        make_request(f"https://{i}.com", token) for i in range(10)
    ]
    _ = await asyncio.gather(*request_coros)


if __name__ == '__main__':
    asyncio.run(main())
