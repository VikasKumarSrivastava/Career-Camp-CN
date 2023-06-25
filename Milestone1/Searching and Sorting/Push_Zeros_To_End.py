# You have been given a random integer array/list(ARR) of size N.
# You have been required to push all the zeros that are present in the array/list to the end of it. 
# Also, make sure to maintain the relative order of the non-zero elements.
# Sample Input 1:
# 1
# 7
# 2 0 0 1 3 0 0
# Sample Output 1:
# 2 1 3 0 0 0 0
from sys import stdin

def pushZerosAtEnd(arr, n):
    k =0
    i = 0
    while i < n:
        if arr[i] != 0:
            arr[i],arr[k] = arr[k],arr[i]
            k = k+1
        i = i +1
