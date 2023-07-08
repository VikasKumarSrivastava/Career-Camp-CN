# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
# Do this recursively.
def solve(ele,x):
    return ele==x
def checkNumber(arr, x):
    # Please add your code here
    i=0
    while i< len(arr):
        ans= solve(arr[i],x)
        if(ans):
            return True
        i+=1
    return False

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
