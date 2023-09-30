# Given an array A and an integer K, print all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Sample Input:
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output:
# 3 3
# 5 1
  
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def printSubset(arr,k,lst):
    n = len(arr)
    if n==0:
        return
    if n==1:
        if arr[0]==k:
            print(k,*lst)
            return
    
    printSubset(arr[:-1],k,lst)
    printSubset(arr[:-1],k-arr[-1],[arr[-1]]+lst)

    if arr[-1] == k:
        print(k,*lst)

def printSubsetMain(arr,k):
    printSubset(arr,k,[])

n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
k = int(input())
printSubsetMain(arr,k)
