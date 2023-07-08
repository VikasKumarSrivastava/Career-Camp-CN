# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.

def solve(a,b):
    return a+b
def sumArray(arr):
    # Please add your code here
    sum = 0
    i=0
    while (i<len(arr)-1):
        sum += solve(arr[i],arr[i+1])
        i=i+2
   # sum += arr[i]
    if len(arr)%2!=0:
        sum += arr[i]
    return sum


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
