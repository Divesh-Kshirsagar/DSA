"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""


def fun(n: int, sum: int = 0) -> int:
    if n < 1:
        print(sum)
        return 0
    return fun(n-1, sum+n)


if __name__ == "__main__":
    fun(5)
