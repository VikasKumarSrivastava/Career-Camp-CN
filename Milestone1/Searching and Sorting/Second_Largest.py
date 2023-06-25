# You have been given a random integer array/list(ARR) of size N.
# You are required to find and return the second largest element present in the array/list.
# Sample Input 1:
# 5
# 4 3 10 9 2
# Sample Output 1:
# 9
from sys import stdin
#MIN_VALUE = -2147483648


def secondLargestElement(arr, n):
    for i in range(n-1 ,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr[n-2]
