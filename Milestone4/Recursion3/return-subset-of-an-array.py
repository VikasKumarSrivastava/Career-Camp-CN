# Given an integer array (of length n), find and return all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12 
# 20 
# 20 12 
# 15 
# 15 12 
# 15 20 
# 15 20 12 
    
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def subset(arr):
    n = len(arr)
    if n<=0:
        output=[ [] ]
        return output

    output = subset(arr[:n-1])

    outputLen=len(output)

    for i in range(0,outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(arr[n-1])
    
    return output

n = int(input())
arr=list(int(i) for i in input().strip().split(' '))
output=subset(arr)

for lst in output:
    for num in lst:
        print(num , end=' ')
    print()
