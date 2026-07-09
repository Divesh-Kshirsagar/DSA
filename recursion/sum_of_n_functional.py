"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""


def fun(n: int) -> int:
    if n == 0:
        return 0
    return n + fun(n - 1)


if __name__ == "__main__":
    print(fun(5))
