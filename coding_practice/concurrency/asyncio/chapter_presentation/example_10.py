import asyncio
import json
import datetime
import time
from urllib.parse import urlencode
import random
import typing as t

import aiohttp
import jwt

"""
ASYNCIO LOCK

DOESNT SEEM TO WORK

Asyncio one process, one thread. Used to run some expensive code once that
is requested by many
"""


class Token:
    TOKEN_DURATION = 30

    def __init__(
        self, sa_content: dict, session: aiohttp.ClientSession
    ) -> None:
        self._lock = asyncio.Lock()
        self._sa_content = sa_content
        self._type = sa_content["type"]
        self._token_uri = sa_content["token_uri"]
        self._session = session
        self._token = None
        self._token_duration = 0
        self._token_acquired_at = datetime.datetime(1994, 5, 29)

    async def get_token(self) -> str:
        """Gets called often by different entities requesting the token"""
        print("Token requested")
        await self._get_token()
        print("Returning the token")
        return self._token

    def _check_if_token_valid(self) -> bool:
        if self._token is None:
            return False
        now = datetime.datetime.utcnow()
        delta = (now - self._token_acquired_at).total_seconds()
        return delta <= self._token_duration / 2

    async def _get_token(self) -> None:
        """Expensive operation that must be done as few times as possible"""
        if self._check_if_token_valid():
            print("Token exists and valid")
            return
        print("Token either doesn't exist or has expired")

        # Only one coro can trigger token refresh instead of all of them
        # triggering the refresh
        if self._lock.locked():
            print("Lock is locked, somebody must be refreshing it already")
            while self._lock.locked():
                await asyncio.sleep(0.1)
        else:
            async with self._lock:
                await self._refresh_token()

    async def _refresh_token(self) -> None:
        now = time.time()
        payload = {
            "aud": self._token_uri,
            "exp": now + Token.TOKEN_DURATION,
            "iat": now,
            "iss": self._sa_content["client_email"],
            "scope": "https://www.googleapis.com/auth/pubsub",
        }
        assertion = jwt.encode(
            payload=payload,
            key=self._sa_content["private_key"],
            algorithm="RS256",
        )
        data = urlencode(
            {
                "assertion": assertion,
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            }
        )
        print("---> Calling GCP backend requesting new token")
        response = await self._session.post(
            url=self._token_uri,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data,
            timeout=30,
        )
        print("---> Response received, parsing")
        content = await response.json()
        self._token = str(content["access_token"])
        self._token_duration = int(content["expires_in"])
        self._token_acquired_at = datetime.datetime.utcnow()


async def worker(i: int, token: Token) -> None:
    while True:
        print(f"Worker {i} requesting the token")
        token = await token.get_token()
        print(f"Worker {i} received the token {token[:20]}")
        await asyncio.sleep(10.0)


def read_sa(filename: str) -> dict:
    print("Opening the file")
    with open(filename, "r") as file:
        content = json.loads(file.read())
    return content


async def kill_tasks(tasks: t.Sequence[asyncio.Task]) -> None:
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)


async def main() -> None:
    content = await asyncio.to_thread(
        read_sa,
        "/Users/etitov1/Coding/gcp-wow-rwds-ai-mlchapter-dev-b90112b5b7af.json",
    )
    async with aiohttp.ClientSession() as session:
        token = Token(content, session)
        worker_tasks = [
            asyncio.create_task(worker(i, token)) for i in range(10)
        ]
        print("Workers started")

        await asyncio.sleep(100)
        await kill_tasks(worker_tasks)
        print("Tasks killed")
    print("Done")


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
