"""
Time complexity = O(2^N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space

Take not take Logic
you will use this logic for picking elements
"""

from typing import Optional

from typing_extensions import List


def fun(alen: int, nums: List, arr: Optional[List] = None, i: int = 0) -> None:
    if arr is None:
        # Use this logic to ensure python only makes one instance of the list
        arr = []
    if i >= alen:
        print(arr)
        return

    # Not Take: pass the arr as it is
    fun(alen, nums, arr, i + 1)

    # Take: add the item recurse, remove and then move back
    arr.append(nums[i])
    fun(alen, nums, arr, i + 1)
    arr.pop()


if __name__ == "__main__":
    arr = [12, 1, 23, 24, 11]
    fun(len(arr), arr)
