"""
Time complexity = O(2^N)
Space Complexity = O(2^N), it is hypothetcial meaning it uses teh stack space
"""


def fun(n: int) -> int:
    if n <= 1:
        return n
    start = fun(n-1)
    last = fun(n-2)
    return start + last


if __name__ == "__main__":
    for i in range(12):
        print(fun(i))
