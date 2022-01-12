import typing as t
from functools import wraps
import time


def timer(func: t.Callable[[t.Any], t.Any]) -> t.Callable[[t.Any], t.Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> t.Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took {time.perf_counter() - start}")
        return result
    return wrapper
