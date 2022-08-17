import typing as t


"""
NOTICE how below we append curr_path to our container of permutations only
when we the length of curr_path reaches the size of nums? This guarantees that
all permutations will be of the same size! We could omit this condition and
add the curr_path to the container every iter which would give us all subsets!

The solutions below pass the available numbers for permutations to every call,
a new copy is created every time, its expensive. Ideally we would love to do it
in place.
"""


# --------- RECURSIVE WITH BACKTRACKING ------------
"""
Unlike the example below, here we aggregate the current path in the same list
instesd of creating a copy every iteration -> its important to pop the last 
value:

! Could be thought of as a tree, say we reach the node sitting on the level
before the last one. From this node we iterate over N kids, each kid will
add an item to the curr_path and then add it to the permutations container.
The kid then backtracks, but the item from the kid is in curr_path, so 
we need to pop it, then the next kid goes etc. Then, the current node
backtracks to one level up, the node above pops its value and considers
other options on the same "level"
"""
def _generate_permutations_backtracking(
    nums: list[t.Any], curr_path: list[t.Any], permutations: list[t.Any]
) -> list[t.Any]:
    if not len(nums):
        permutations.append(curr_path[:])
    else:
        for i in range(len(nums)):
            remaining_nums = nums[:i] + nums[i + 1:]
            curr_path.append(nums[i])
            _generate_permutations_backtracking(
                remaining_nums,
                curr_path,  # HERE WE PASS ORIGINAL CURR_PATH, NOT COPY!
                permutations
            )
            curr_path.pop()
    return permutations


def recursive_backtracking_permute(nums: list[t.Any]) -> list[t.Any]:
    return _generate_permutations_backtracking(nums, [], [])


# --------- RECURSIVE WITHOUT BACKTRACKING (IMPLICIT STACK) ------------
"""
Recursive without backtracking (implicit stack)

This is super slow T: O(N!) but clear

dfs(nums = [1, 2, 3] , path = [] , result = [] )
|
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
|
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
|
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
"""
def _generate_permutations(
    nums: list[t.Any], curr_path: list[t.Any], permutations: list[t.Any]
) -> None:
    length = len(nums)
    if not length:
        permutations.append(curr_path)

    for i in range(length):
        updated_curr_path = curr_path + [nums[i]]
        _generate_permutations(
          nums=nums[: i] + nums[i+1:],
          curr_path=updated_curr_path,  # ! HERE WE PASS A COPY
          permutations=permutations
        )


def recursive_implicit_permute(nums: list[t.Any]) -> list[t.Any]:
    permutations = []
    _generate_permutations(nums, [], permutations)
    return permutations


# --------- DFS Iterative with Explicit Stack ---------

def iterative_dfs(nums: list[t.Any]) -> list[t.Any]:
    permutations = []
    stack = [(nums, [])]
    while len(stack):
        nums, curr_path = stack.pop()

        if not len(nums):
            permutations.append(curr_path)
        else:
            for i in range(len(nums)):
                remaining_nums = nums[:i] + nums[i + 1:]
                stack.append((remaining_nums, curr_path + [nums[i]]))

    return permutations


# --------- BFS Iterative with a Queue ---------

def iterative_bfs(nums: list[t.Any]) -> list[t.Any]:
    from queue import Queue

    permutations = []
    queue = Queue()
    queue.put((nums, []))
    while queue.qsize():
        nums, curr_path = queue.get()

        if not len(nums):
            permutations.append(curr_path)
        else:
            for i in range(len(nums)):
                remaining_nums = nums[:i] + nums[i + 1:]
                queue.put((remaining_nums, curr_path + [nums[i]]))

    return permutations


def main():
    nums = [1, 2, 3]

    print(recursive_backtracking_permute(nums))
    print(recursive_implicit_permute(nums))
    print(iterative_dfs(nums))
    print(iterative_bfs(nums))


if __name__ == '__main__':
    main()
