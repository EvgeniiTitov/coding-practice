
def compressedString(message: str) -> str:
    if not message:
        return ""

    chars_stack = []
    for char in message:
        if not len(chars_stack):
            chars_stack.append(f"1_{char}")
        else:
            prev_char_data = chars_stack[-1]
            prev_char_counter, prev_char = prev_char_data.split("_")
            if prev_char != char:
                chars_stack.append(f"1_{char}")
            else:
                chars_stack.pop()
                chars_stack.append(f"{int(prev_char_counter) + 1}_{char}")

    str_out = []
    for char_occurences in chars_stack:
        times_seen, char = char_occurences.split("_")
        if times_seen == "1":
            str_out.append(char)
        else:
            str_out.append(f"{char}{times_seen}")

    return "".join(str_out)


def isPangram(pangram: list[str]) -> str:

    def _check_if_pangram(string: str) -> bool:
        curr_chars = set()
        for char in string:
            if not char.isalnum():
                continue
            curr_chars.add(char)
        return len(curr_chars.intersection(alphabet)) == 26

    a_num, z_num = ord("a"), ord("z")
    alphabet = set(chr(i) for i in range(a_num, z_num + 1))
    out = []
    for string in pangram:
        if _check_if_pangram(string):
            out.append("1")
        else:
            out.append("0")
    return "".join(out)


def minSum(num: list[int], k: int) -> int:
    # Operation - must be done k times.
    #   1. Remove element from the array
    #   2. Divide it by 2
    #   3. Insert the ceil() of the division back into the array

    # Task - minimise the SUM of the array

    import heapq
    import math

    num = [-value for value in num]  # Simulate MAX heap
    heapq.heapify(num)
    for _ in range(k):
        curr_largest = -heapq.heappop(num)
        new_val = math.ceil(curr_largest / 2)
        heapq.heappush(num, -new_val)

    return sum(-value for value in num)


def consecutive(num: int) -> int:

    def _reach_num(num: int, curr: int) -> int:
        pass
    pass


# Failed 1 test
def isPossible(a: int, b: int, c: int, d: int) -> str:
    # Allowed moves:
    #   (x, y) -> (x + y, y)
    #   (x, y) -> (x, x + y)

    def _cache(func):
        _cache = {}
        def wrapper(curr: tuple[int, int], dest: tuple[int, int]) -> bool:
            if curr not in _cache:
                _cache[curr] = func(curr, dest)
            return _cache[curr]
        return wrapper

    @_cache
    def _reach_destination(
        curr: tuple[int, int], dest: tuple[int, int]
    ) -> bool:
        curr_x, curr_y = curr
        boundary_x, boundary_y = dest

        # Base cases
        if curr_y > boundary_y or curr_x > boundary_x:
            return False

        # Check if we've reached the destination
        if curr == dest:
            return True

        # Probe the space for the potential solution
        move_1 = _reach_destination(
            curr=(curr_x + curr_y, curr_y), dest=dest
        )
        move_2 = _reach_destination(
            curr=(curr_x, curr_x + curr_y), dest=dest
        )

        return move_1 or move_2

    start = (a, b)
    dest = (c, d)
    return  "Yes" if _reach_destination(start, dest) else "No"


# Passed all
def isPossible(a: int, b: int, c: int, d: int) -> str:
    from queue import Queue

    queue = Queue()
    queue.put((a, b))
    while queue.qsize():
        curr_a, curr_b = queue.get()

        # Base cases
        if curr_a > c or curr_b > d:
            continue
        elif curr_a == c and curr_b == d:
            return "Yes"

        # Probe the space
        queue.put((curr_a + curr_b, curr_b))
        queue.put((curr_a, curr_a + curr_b))

    return "No"


if __name__ == '__main__':
    # print(compressedString("abaabbbc"))
    # print(isPangram([
    #     "we promptly judged antique ivory buckles for the next prize",
    #     "we promptly judged antique ivory buckles for the prizes",
    #     "the quick brown fox jumps over the lazy dog",
    #     "the quick brown fox jump over the lazy dog",
    #
    # ]))

    # print(minSum(
    #     num=[10, 20, 7],
    #     k=4
    # ))

    print(isPossible(1, 1, 5 ,2))
