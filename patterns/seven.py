def pattern(n: int) -> None:
    if n < 1:
        print("Wont work!")
        return
    k: int = 1
    for i in range(n,0,-1):
        r: str = (" "*(i-1)) + ("*"*k) +  (" "*(i-1)) 
        print(r)
        k += 2


if __name__ == "__main__":
    n: int = int(input("Enter a number: "))
    pattern(n)