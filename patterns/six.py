from typing_extensions import List


def pattern(n: int) -> None:
    if n < 1:
        print("Wont work!")
        return
    arr:List[int] = []
    for i in range(1, n+1):
        arr.append(i)
    for i in range(len(arr)):
        s = ""
        for j in arr:
            s += str(j)
        print(s)
        arr.pop()


if __name__ == "__main__":
    n: int = int(input("Enter a number: "))
    pattern(n)