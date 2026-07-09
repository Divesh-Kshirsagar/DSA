def pattern(n: int) -> None:
    if n < 1:
        print("Wont work!")
        return
    s = ""
    for i in range(1, n+1):
        s = s+str(i)
        print(f"{s}")


if __name__ == "__main__":
    n: int = int(input("Enter a number: "))
    pattern(n)