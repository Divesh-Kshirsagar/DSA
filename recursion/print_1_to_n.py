"""
Time complexity = O(N)
Space Complexity = O(N), it is hypothetcial meaning it uses teh stack space
here the concept of backtracking is used
When calling the print() after the recursion call we are ensuring that the print is called after the base condition is met
"""

def fun(n: int):
    if n==0:
        return 
    fun(n-1)
    print(n)

if __name__=="__main__":
    fun(5)