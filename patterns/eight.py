def pattern(n: int) -> None:
    if n < 1:
        print("Wont work!")
        return
    k: int = n
    for i in range(n+1):
        r: str = (" "*(i)) + ("*"*k) +  (" "*(i)) 
        print(r)
        k -= 2


if __name__ == "__main__":
    n: int = int(input("Enter a number: "))
    pattern(n)