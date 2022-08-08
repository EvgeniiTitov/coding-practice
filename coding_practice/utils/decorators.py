import typing as t
from functools import wraps
import time


__all__ = ["timer", "times_called"]


def timer(func: t.Callable[[t.Any], t.Any]) -> t.Callable[[t.Any], t.Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> t.Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took: {time.perf_counter() - start}")
        return result

    return wrapper


def times_called(func: t.Callable) -> t.Callable:
    counter = 0

    @wraps(func)
    def wrapper(*args, **kwargs) -> t.Any:
        nonlocal counter
        result = func(*args, **kwargs)
        counter += 1
        print(f"Func: {func.__name__} called {counter} times")
        return result

    return wrapper
