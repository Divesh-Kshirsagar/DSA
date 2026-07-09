"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""

from typing import List


def fun(arr: List, rev: List,  i: int = 0):
    if i >= len(arr):
        return
    fun(arr, rev, i + 1)
    rev.append(arr[i])


if __name__ == "__main__":
    arr = [12, 123, 134, 24, 12234]
    rev_arr = []
    fun(arr, rev_arr)
    print(rev_arr)