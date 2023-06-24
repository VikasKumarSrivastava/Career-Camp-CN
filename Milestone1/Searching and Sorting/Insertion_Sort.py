# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Insertion Sort'.
# Sample Input 1:
# 1
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
from sys import stdin

def insertionSort(arr, n) :  
    #Your code goes here
    for i in range(1,n):
        j = i-1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = temp



