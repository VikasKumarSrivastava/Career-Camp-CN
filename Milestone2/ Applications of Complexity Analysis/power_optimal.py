def power(x, n):
    # Please add your code here
    if n==0:
        return 1
    small_output = power(x,n//2)
    if n%2==0:
        return small_output * small_output
    else:
        return x*small_output*small_output
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
