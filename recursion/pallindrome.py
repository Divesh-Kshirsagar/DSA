"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""


def fun(w: str, i: int = 0) -> bool:
    if i >= len(w) / 2:
        return True
    if w[i] != w[len(w) - i - 1]:
        return False
    return fun(w, i + 1)


if __name__ == "__main__":
    word = "MADAMA"
    print(fun(word))
