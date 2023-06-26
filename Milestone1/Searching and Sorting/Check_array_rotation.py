# You have been given an integer array/list(ARR) of size N. 
# It has been sorted(in increasing order) and then rotated by some number 'K' (K is greater than 0) in the right hand direction.
# Your task is to write a function that returns the value of 'K', that means, the index from which the array/list has been rotated.
#Sample Input 1:
# 1
# 6
# 5 6 1 2 3 4
# Sample Output 1:
# 2
from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    min_ele = 999999
    ans = 0
    for i in range(0,n):       
        if arr[i] < min_ele:
            min_ele = arr[i]
            ans = i
    return ans
