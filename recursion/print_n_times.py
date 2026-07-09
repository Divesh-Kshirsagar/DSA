"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
"""

def fun(n: int, name: str):
    if n==0:
        return 
    print(name)
    return fun(n-1, name)

if __name__=="__main__":
    fun(5, "Divesh")