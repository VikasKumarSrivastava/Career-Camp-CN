# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here
    for i in range (0,n):
        min_index= i
        for j in range (i+1,n):
            if arr[j] < arr[min_index] :
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
