"""
Time complexity = O(2^N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space

Take not take Logic
you will use this logic for picking elements
"""

from typing import Optional

from typing_extensions import List


def fun(nums: List, k, arr: Optional[List] = None, ind: int = 0, sum: int = 0) -> None:
    if arr is None:
        arr = []
    if ind == len(nums):
        if sum == k:
            print(arr)
        return

    # Take 
    arr.append(nums[ind])
    sum += nums[ind]
    fun(nums, k, arr, ind + 1, sum)
    # Not take it
    arr.pop()
    sum -= nums[ind]
    fun(nums, k, arr, ind + 1, sum)


if __name__ == "__main__":
    arr = [1, 1, 2, 0]
    k = 3
    fun(arr, k)
