import typing as t

from memory_profiler import profile


'''
Test inspired by https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

Apparently reversed(range()) do not accumulate the entire sequence in memory
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37  12.976562 MiB  12.976562 MiB           1   @profile(precision=6)
    38                                         def main():
    39  12.976562 MiB   0.000000 MiB           1       n = int(input())
    40                                         
    41  13.054688 MiB   0.039062 MiB      100001       for number in reversed(range(n)):
    42  13.054688 MiB   0.039062 MiB      100000           print(number)
    
VS

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37  13.066406 MiB  13.066406 MiB           1   @profile(precision=6)
    38                                         def main():
    39  13.066406 MiB   0.000000 MiB           1       n = int(input())
    40                                         
    41  16.972656 MiB   3.855469 MiB      100001       for number in reversed(list(range(n))):
    42  16.972656 MiB   0.050781 MiB      100000           print(number)
    
VS custom written generator

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37  12.996094 MiB  12.996094 MiB           1   @profile(precision=6)
    38                                         def main():
    39  12.996094 MiB   0.000000 MiB           1       n = int(input())
    40                                         
    41  13.074219 MiB   0.035156 MiB      100001       for number in get_next_number(n - 1):
    42  13.074219 MiB   0.042969 MiB      100000           print(number)
'''

def get_next_number(n: int) -> t.Iterator[int]:
    while n >= 0:
        yield n
        n -= 1


@profile(precision=6)
def main():
    n = int(input())

    for number in get_next_number(n - 1):
        print(number)


if __name__ == '__main__':
    main()
