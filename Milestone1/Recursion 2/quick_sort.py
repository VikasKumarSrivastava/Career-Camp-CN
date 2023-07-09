# QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot
# and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
# Working of Quick Sort:
  # The key process in quickSort is a partition(). The target of partitions is to place the pivot (any element can be chosen to be a pivot) 
  # at its correct position in the sorted array and put all smaller elements to the left of the pivot, 
  # and all greater elements to the right of the pivot.
  # Partition is done recursively on each side of the pivot after the pivot is placed in its correct position 
  # and this finally sorts the array.
# Time Complexity:
  # Best Case: \omega (N * log N)
  # Average Case: \Theta (N * logN)
  # Worst Case: O(N2)
# Auxiliary Space: O(log(N))
# It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved 
# in the sorted output in case of quick sort, 
# because here we are swapping elements according to the pivot’s position (without considering their original positions).
# For more details visit: https://www.geeksforgeeks.org/quick-sort/
# Important article : https://www.geeksforgeeks.org/why-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists/
"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""


def partitionArray(input: [int], start: int, end: int) -> int:
    # Write your code here
    pivot= input[start]
    c=0
    for i in range(start+1,end+1):
        if input[i] < pivot:
            c+=1
    input[start+c],input[start] = input[start],input[start+c]
    pivot_index = start+c
    i = start
    j= end
    while i< j:
        if input[i] < pivot:
            i +=1
        elif input[j] >= pivot:
            j-=1
        else:
            input[i],input[j]=input[j],input[i]
            i+=1
            j-=1
    return pivot_index

def quickSort(input: [int], start: int, end: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if start >= end:
        return
    pi= partitionArray(input,start,end)
    quickSort(input,start,pi-1)
    quickSort(input,pi+1,end)
