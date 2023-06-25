# You have been given a random integer array/list(ARR) of size N.
# Write a function that rotates the given array/list by D elements(towards the left).
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output 1:
# 3 4 5 6 7 1 2
from sys import stdin

def swapElements(arr, start, end) :
    arr[start], arr[end] = arr[end], arr[start] 
    
def reverse(arr, start, end): 
    while(start < end):
        swapElements(arr, start, end)
        start += 1
        end -= 1 
def rotate(arr, n, d):
    #Your code goes here
    if n == 0 :
        return
    if d >= n and n != 0 :
        d = d % n
    reverse(arr, 0, n - 1) 
    reverse(arr, 0, n - d - 1) 
    reverse(arr, n - d, n - 1) 
