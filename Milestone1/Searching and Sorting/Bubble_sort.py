#Provided with a random integer array/list(ARR) of size N, you must sort this array using 'Bubble Sort'.
# Input: ‘N’ = 7
# 'ARR' = [2, 13, 4, 1, 3, 6, 28]
# Output: [1 2 3 4 6 13 28]
# Explanation: After applying 'bubble sort' on the input array, the output is [1 2 3 4 6 13 28].

def bubbleSort(arr: [int], size: int):
    # Your code goes here.
    for i in range(size):
        for j in range(size-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
