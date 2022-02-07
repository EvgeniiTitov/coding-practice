"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if (i + j + k) != n
    ]
    print(result)

    # results = []
    # for i in range(x + 1):
    #     for j in range(y + 1):
    #         for k in range(z + 1):
    #            if i + j + k != n:
    #             results.append([i, j, k])
    # print(results)
