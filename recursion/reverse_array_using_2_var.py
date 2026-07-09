"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""

from typing import List


def fun(arr: List, left : int, right:int) -> None:
    if left>=right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    fun(arr, left+1, right-1)


if __name__ == "__main__":
    arr = [12, 123, 134, 24, 12234]
    fun(arr, 0, len(arr)-1)
    print(arr)