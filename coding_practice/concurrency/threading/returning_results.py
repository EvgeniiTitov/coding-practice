import threading
from concurrent.futures import Future, as_completed
import typing as t
from traceback import format_exc

import requests


"""
I forgot about that - https://github.com/EvgeniiTitov/utility/blob/master/random/threaded.py
Just go there
"""


LOCK = threading.Lock()


def do_request(url: str, *args, **kwargs) -> tuple:
    with LOCK:
        print("Doing request to:", url)
    response = requests.get(url, *args, **kwargs)
    return response.status_code, response.text


def run_func_async(func: t.Callable, *args, **kwargs) -> Future:
    future = Future()
    thread = threading.Thread(
        target=lambda: _run_function(future, func, *args, **kwargs),
        daemon=True
    )
    thread.start()
    return future


def _run_function(future: Future, func: t.Callable, *args, **kwargs) -> None:
    future.set_running_or_notify_cancel()
    try:
        result = func(*args, **kwargs)
    except BaseException as e:
        e.traceback = format_exc()
        future.set_exception(e)
    else:
        future.set_result(result)


def threading_1():
    fut1 = run_func_async(do_request, "https://api.agify.io?name=eugene")
    fut2 = run_func_async(do_request, "https://api.genderize.io?name=eugene")
    fut3 = run_func_async(do_request, "https://api.nationalize.io?name=eugene")
    fut4 = run_func_async(do_request, "https://broken.link?name=torch")
    for fut in as_completed((fut1, fut2, fut3, fut4)):
        try:
            print("Result: ", fut.result())
        except Exception:
            print("Error occurred:", fut.exception())


def sequential():
    resp_1 = do_request("https://api.agify.io?name=eugene")
    print(resp_1)
    resp_2 = do_request("https://api.agify.io?name=daria")
    print(resp_2)
    resp_3 = do_request("https://api.agify.io?name=torch")
    print(resp_3)


if __name__ == '__main__':
    # sequential()
    threading_1()
