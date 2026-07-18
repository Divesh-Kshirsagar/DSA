"""
In this algo you compare elements with the adjacent element sending the biggest element in the back
Time complexity = O(N^2)
Space complexity = O(1)
"""

import time
from typing import List


def fun(arr: List[int], aesc: int = 0) -> List[int]:
    n: int = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if not aesc:
                if arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


if __name__ == "__main__":
    start_time = time.process_time()
    arr = [12, 23, 12, 112, 11, 5, 6, 778]
    print(fun(arr))
    end_time = time.process_time()

    print(f"CPU execution time: {end_time - start_time} seconds")
