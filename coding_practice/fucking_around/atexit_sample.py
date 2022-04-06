import time
import typing as t
import atexit

import requests


"""
TODO: Add this to your WXGMeta client!
"""


class RESTClient:
    def __init__(self) -> None:
        self._session = requests.Session()

    def close(self) -> None:
        self._session.close()
        print("RESTClient closed the session")


class Experiment:
    def __init__(self, experiment_id: t.Optional[str] = None) -> None:
        self._rest_client = RESTClient()
        if experiment_id:
            print(f"Connecting to the existing experiment: {experiment_id}")
        else:
            print("Creating new experiment")
        atexit.register(self.close)

    def log_kv(self, k, v) -> None:
        print("Logging KV")

    def close(self):
        print("Close method triggered automatically")
        self._rest_client.close()


def main() -> None:
    exp = Experiment()
    exp.log_kv("one", 1)
    time.sleep(1.0)
    exp.log_kv("two", 2)


if __name__ == "__main__":
    main()
