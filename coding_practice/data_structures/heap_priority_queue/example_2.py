import datetime
import heapq
import typing as t


"""
Since priority queues are so often used to merge sorted sequences, the Python 
heapq module has a ready-made function, merge(), for using heaps to merge 
several iterables. merge() assumes its input iterables are already sorted and 
returns an iterator, not a list.

The inputs to merge() in this example are infinite generators. The return 
value assigned to the variable unified is also an infinite iterator. This 
iterator will yield the emails to be sent in the order of the future timestamps.

Stdout:
(datetime.datetime(2022, 7, 4, 13, 50, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 14, 5, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 14, 15, 23, 177541), 'Slow Email')
(datetime.datetime(2022, 7, 4, 14, 20, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 14, 35, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 14, 50, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 14, 55, 23, 177541), 'Slow Email')
(datetime.datetime(2022, 7, 4, 15, 5, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 15, 20, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 15, 35, 23, 177534), 'Fast Email')
(datetime.datetime(2022, 7, 4, 15, 35, 23, 177541), 'Slow Email')

"""


def email(
    frequency: datetime.timedelta, details: str
) -> t.Iterator[t.Tuple[datetime.datetime, str]]:
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details


def main():
    fast_email = email(datetime.timedelta(minutes=15), "Fast Email")
    slow_email = email(datetime.timedelta(minutes=40), "Slow Email")

    unified = heapq.merge(*(fast_email, slow_email))

    for i, email_to_send in enumerate(unified):
        print(email_to_send)
        if i == 10:
            break


if __name__ == "__main__":
    main()
