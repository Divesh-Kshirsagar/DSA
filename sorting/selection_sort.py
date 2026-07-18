"""
Easiest of all the sorting  algo
In this algo you compare each element until you find the biggest and send it to the back
Time complexity = O(N^2)
Space complexity = O(1)
"""

import time
from typing import List


def fun(arr: List[int], aesc: int = 0) -> List[int]:
    n: int = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if not aesc:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == "__main__":
    start_time = time.process_time()
    arr = [12, 23, 12, 112, 11, 5, 6, 778]
    print(fun(arr, 1))
    end_time = time.process_time()

    print(f"CPU execution time: {end_time - start_time} seconds")
