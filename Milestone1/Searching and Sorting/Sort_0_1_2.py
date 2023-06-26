# You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. 
# Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words, 
# you will be visiting each element in the array/list just once.
# Sample Input 1:
# 1
# 7
# 0 1 2 0 2 0 1
# Sample Output 1:
# 0 0 0 1 1 2 2 
from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    low = 0 
    mid = 0
    high = n -1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid],arr[low]= arr[low],arr[mid]
            low =low+1
            mid= mid+1
        elif arr[mid] ==1:
            mid = mid + 1
        else:
            arr[mid],arr[high] = arr[high],arr[ mid]
            high = high-1
