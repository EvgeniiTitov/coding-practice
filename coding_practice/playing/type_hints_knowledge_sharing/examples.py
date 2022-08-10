from __future__ import annotations

import threading
import time
from typing import (
    List,
    Union,
    Tuple,
    Iterator,
    Optional,
    Callable,
    Mapping,
    Any,
    Sequence,
    Iterable,
    Literal,
    MutableMapping,
    Sized,
    TypeVar,
    Generic,
    Protocol
)
import os
from queue import Queue
from dataclasses import dataclass
from logging import Logger

import numpy as np
import pandas as pd
# import cv2



# ------------------ Simple examples ------------------
def greet_by_name(name: str) -> None:
    print("Hello", name)


def plus(num1: int, num2: int) -> int:
    return num1 + num2


def add_up_numbers(numbers: List[int]) -> int:
    return sum(numbers)


def get_sum_and_count(numbers: List[Union[int, float]]) -> Tuple[int, float]:
    length = len(numbers)
    sum_ = sum(numbers)
    return length, sum_


def get_sum_and_count_2(numbers: list[int | float]) -> tuple[int, float]:
    length = len(numbers)
    sum_ = sum(numbers)
    return length, sum_


# ------------------ Optional ------------------
class Logger:

    def __init__(self, name: str) -> None:
        self._name = name

    def info(self, text: str) -> None:
        print(f"Logger {self._name} -- {text}")


# def process_files(folder: str, logger: Optional[Logger] = None) -> None:
#     for filepath in get_file_paths(folder):
#         if logger:
#             logger.info(f"Processing file: {filepath}")
#         else:
#             print(f"Processing file: {filepath}")


def process_files(folder: str, logger: Logger | None = None) -> None:
    for filepath in get_file_paths(folder):
        if logger:
            logger.info(f"Processing file: {filepath}")
        else:
            print(f"Processing file: {filepath}")


# ------------------ Iterators ------------------
def get_file_paths(folder: str) -> Iterator[str]:
    for filename in os.listdir(folder):
        yield os.path.join(folder, filename)


# ------------------ Alias ------------------
GPUMetrics = List[MutableMapping[str, Any]]


Batch = list[np.ndarray]


# def show_batch(
#     images: Batch, window_name: str = "", horizontal: bool = True
# ) -> None:
#     stacked = np.concatenate(images, axis=1 if horizontal else 0)
#     cv2.imshow(window_name, stacked)
#     cv2.waitKey(0)


Vector = list[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


# ------------------ Callables ------------------


# Callable[[int, int], int]
def multiple_numbers(num1: int, num2: int) -> int:
    return num1 * num2


@dataclass
class Message:
    source: str
    destination: str
    content: str


def process_message(message: Message) -> None:
    print("Processing message:", message)


def worker(queue: Queue, callback: Callable[[Message], None]):
    while True:
        item = queue.get()
        callback(item)
        queue.task_done()


def timer(func: Callable) -> Callable[..., Any]:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} "
              f"took {time.time() - start} sec")
        return result
    return wrapper


@timer
def count() -> None:
    for i in range(10_000):
        _ = i ** i


# ------------------ Duck typing ------------------

def process_items(items: Iterable[int]) -> None:
    for item in items:
        print("Processing item:", item)


def extend_metrics(metrics: Mapping[str, Any]) -> None:
    metrics["ABC"] = 123


class CustomObject:
    def __init__(self, name: str):
        self.name = name

    def __len__(self):
        return 1


def show_length(obj: Sized) -> int:
    return len(obj)


# ------------------ Literal ------------------


def upload_df_to_bq(
    df: pd.DataFrame, mode: Literal["APPEND", "TRUNCATE", "EMPTY"]
) -> None:
    print("Uploading df with mode:", mode)

    print(df.columns)


# ------------------ Generics ------------------

T = TypeVar("T")


def get_first(items: Sequence[T]) -> T:
    return items[0]


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

#
# T = TypeVar('T')  # Can be anything
# S = TypeVar('S', bound=str)  # Can be any subtype of str
# A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
#
#
# def repeat(x: T, n: int) -> Sequence[T]:
#     """Return a list containing n references to x."""
#     return [x]*n
#
#
# def print_capitalized(x: S) -> S:
#     """Print x capitalized, and return x."""
#     print(x.capitalize())
#     return x
#
#
# def concatenate(x: A, y: A) -> A:
#     """Add two strings or bytes objects together."""
#     return x + y


# ------------------ Custom objects and Protocols ------------------


class BaseModel(Protocol):

    def predict(self, df: pd.DataFrame) -> Any:
        ...


class KNNModel(BaseModel):

    def predict(self, df: pd.DataFrame) -> Any:
        print("KNN predicting...")


class SVMModel(BaseModel):

    def predict(self, df: pd.DataFrame) -> Any:
        print("SVM predicting...")


class RandomModel:

    def score(self, df: pd.DataFrame, range: tuple[int, int]) -> float:
        print("RandomModel predicting")
        return 0.0


def run_model(data: pd.DataFrame, model: BaseModel):
    model.predict(data)



def main():
    # file_iterator = get_file_paths("/Users/etitov1/Downloads")
    # print(next(file_iterator))
    # print(next(file_iterator))
    # print(next(file_iterator))

    # image1 = np.zeros((100, 100, 3), dtype=np.uint8)
    # image2 = np.zeros((100, 100, 3), dtype=np.uint8)
    # image3 = np.zeros((100, 100, 3), dtype=np.uint8)
    # show_batch([image1, image2, image3])
    #
    # show_batch()

    # queue = Queue()
    # thread = threading.Thread(target=worker, args=(queue, process_message))

    # items_list = [1, 2, 3, 4, 5]
    # items_tuple = (1, 2, 3, 4, 5)
    # items_set = {1, 2, 3, 4, 5}
    # items_dict = {1: "", 2: "", 3: "", 4: "", 5: ""}
    # for items in items_list, items_tuple, items_set, items_dict:
    #     process_items(items)

    # count()

    # df = pd.DataFrame()
    # upload_df_to_bq(df, mode="APPEND")
    # upload_df_to_bq(df, mode="RANDOM")

    # show_length(CustomObject("name"))

    df = pd.DataFrame()
    model = KNNModel()
    run_model(df, model)

    random_model = RandomModel()
    run_model(df, random_model)











if __name__ == '__main__':
    main()
