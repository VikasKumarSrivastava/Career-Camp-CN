# Merge sort is a recursive algorithm that continuously splits the array in half until it cannot be further divided i.e., 
# the array has only one element left (an array with one element is always sorted). 
# Then the sorted subarrays are merged into one sorted array.
# for more details visit: https://www.geeksforgeeks.org/merge-sort/
# Time Complexity : O(nlog(n))
#Auxillary space : O(n)
#A stable algorithm, which means it maintains the relative order of equal elements in the input array.
#Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. 
    #This can be a disadvantage in applications where memory usage is a concern.
def merge(arr1,arr2,arr):
    i=0
    j=0
    k=0
    while i <len(arr1) and j <len(arr2):
        if arr1[i]>arr2[j]:
            arr[k]=arr2[j]
            k+=1
            j+=1
        else:
            arr[k] =arr1[i]
            k+=1
            i+=1
    while i < len(arr1):
        arr[k]=arr1[i]
        k+=1
        i+=1
    while j < len(arr2):
        arr[k]= arr2[j]
        k+=1
        j+=1
    return arr
def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if len(arr) == 0 or len(arr)==1:
        return
    mid = len(arr)//2
    arr1= arr[0:mid]
    arr2=arr[mid:]
    mergeSort(arr1,0,mid-1)
    mergeSort(arr2,mid,len(arr)-1)
    merge(arr1,arr2,arr)
