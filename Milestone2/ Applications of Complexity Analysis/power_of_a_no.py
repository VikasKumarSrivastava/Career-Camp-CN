# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
# Do this recursively.
def power(x, n):
    # Please add your code here
    if n==0:
        return 1
    return x * power(x,n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
