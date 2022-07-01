from typing import List


"""
Items In Containers

Summary:
    My solution (didn't pass test) - 2 pointers, left finds |, start moving
    right till it finds |, then count *s in between, left = right, right  += 1.
    If left is not on a pipe, move left and right one step ->. If left found |
    but right never found one, items counted are not valid.


An item is represented as an asterisk ( * = ascii decimal 42). A compartment 
is represented as a pair of pipes that may or may not have items between them 
( | = ascii decimal 124).

Example 1:
Input: s = |**|*|*, startIndices = [1, 1], endIndices = [5, 6]
Output: [2, 3]
Explanation:
The string has a total of 2 closed compartments, one with 2 items and one with 1 item.
For the first pair of indices, (0, 4), the substring |**|*. There are 2 items in a compartment.
For the second pair of indices, (0, 6), the substring is |**|*|* and there are 2 + 1 = 3 items in compartments.
Both of the answers are returned in an array, [2, 3]

Example 2:
Input: s = *|*|, startIndices = [1], endIndices = [3]
Output: [1]
Explanation:
the substring from index = 1 to index = 3 is |*|. There is one compartments with one item in this string.
Constraints:
1 <= m, n <= 10^5
1 <= startIndices[i] <= endIndices[i] <= n
Each character or s is either * or |

"""


# Mine: Seems to be working, yet it didn't pass the tests. T: O(N)
def _count_items(s):
    if not s:
        return 0
    length = len(s)
    left, right = 0, 1
    items_counted_out = 0
    current_items = 0
    while right < length:
        if s[left] != "|":
            left += 1
            right += 1
            continue

        valid_items = False
        while right < length:
            if s[right] == "|":
                valid_items = True
                break
            current_items += 1
            right += 1

        if valid_items:
            items_counted_out += current_items

        current_items = 0
        left = right
        right += 1

    return items_counted_out


# From folks on the internet - how is this better?
def cntitems2(items: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
    ln = len(items)
    # pre-calc left-most pipe location and sum of stars arrays
    stars = [0] * (ln+1)
    lftpipeidx = [-1] * (ln+1)
    for i, ch in enumerate(items,1):
        if ch == "|":
            stars[i] = stars[i-1]
            lftpipeidx[i] = i
        else:  # ch == *
            stars[i] = stars[i-1] + 1
            lftpipeidx[i] = lftpipeidx[i-1]
    if lftpipeidx[-1] == -1:
        return [0]*len(startIndices)

    # pre-calc right-most pipe location
    rgtpipeidx = [ln+1] * (ln+1)
    for i in range(ln-1,-1,-1):
        if items[i] == '|':
            rgtpipeidx[i+1] = i+1
        else:
            rgtpipeidx[i+1] = rgtpipeidx[i+2] if i < ln-1 else ln+1

    # calc answer as difference between num. of stars b/w right and left pipes.
    # right pipe is the left-most pipe from the end index, left pipe is the right-most one from the start index
    ans = []
    for i in range(len(startIndices)):
        si, ei = startIndices[i], endIndices[i]
        lftpipe = rgtpipeidx[si]
        rgtpipe = lftpipeidx[ei]
        ans.append(stars[rgtpipe] - stars[lftpipe] if lftpipe < rgtpipe else 0)
    return ans


def main():
    s = "|||||*|"
    print(_count_items(s))


if __name__ == '__main__':
    main()
