def pattern(n: int) -> None:
    if n < 1:
        print("Wont work!")
        return
    for i in range(n):
        print("*" * i)


if __name__ == "__main__":
    n: int = int(input("Enter a number: "))
    pattern(n)