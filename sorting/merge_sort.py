"""
It uses divide and merge approach
Pattern is simple: divide, sort(using pointers), merge
Here the core word is hypothetical 
The division and merging is happening entirely virtually
Time complexity = O(N.log(N))
Space complexity = O(N)
"""

import time
from typing import List


def fun(arr: List[int], low: int, high: int):
    if low >= high:
        return
    mid: int = (high + low) // 2
    fun(arr, low, mid)
    fun(arr, mid + 1, high)
    sort(arr, low, mid, high)
    return arr


def sort(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high):
        arr[i] = temp[i - low]


if __name__ == "__main__":
    start_time = time.process_time()
    arr = [12, 23, 12, 112, 11, 5, 6, 778]
    print(fun(arr, 0, len(arr) - 1))
    end_time = time.process_time()

    print(f"CPU execution time: {end_time - start_time} seconds")
