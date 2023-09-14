# Given an integer array of size N. Sort this array (in decreasing order) using heap sort.
# Note: Space complexity should be O(1)
# Sample Input 1:
# 6 
# 2 6 8 5 4 3
# Sample Output 1:
# 8 6 5 4 3 2

def down_heapify(arr,i,n):
    pI=i
    lci = 2*pI+1
    rci=2*pI+2

    while lci < n:
        minIndex = pI

        if arr[minIndex] > arr[lci]:
            minIndex = lci
        if rci < n and arr[minIndex] > arr[rci]:
            minIndex = rci
        
        if minIndex == pI:
            return
        
        arr[minIndex],arr[pI]=arr[pI],arr[minIndex]

        pI = minIndex
        lci= 2*pI+1
        rci=2*pI+2
    return
def heapSort(arr):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        down_heapify(arr,i,n)
    
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heapify(arr,0,i)
    return

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')
