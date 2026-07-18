"""
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

import time
from typing import List


def fun(arr: List[int], low: int, high: int):
    if low >= high:
        return
    pivot = sort(arr, low, high)
    fun(arr, pivot+1, high) 
    fun(arr, low, pivot-1)
    return arr


def sort(arr, low, high) -> int:
    pivot = low
    i, j = low, high
    while(i<j):
        while(arr[i]<=arr[pivot] and i<high):
            i+=1
        while(arr[j]>=arr[pivot] and j>low):
            j-=1
        # swap when i and j hasnt crossed the paths
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[j] = arr[j], arr[pivot]

    return j


if __name__ == "__main__":
    start_time = time.process_time()
    arr = [12, 23, 12, 112, 11, 5, 6, 778]
    print(fun(arr, 0, len(arr) - 1))
    end_time = time.process_time()

    print(f"CPU execution time: {end_time - start_time:.7f} seconds")
