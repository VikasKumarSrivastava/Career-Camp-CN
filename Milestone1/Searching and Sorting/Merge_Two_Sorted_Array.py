# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, 
# merge them into a third array/list such that the third array is also sorted.
# Sample Input 1 :
# 1
# 5
# 1 3 4 7 11
# 4
# 2 4 6 13
# Sample Output 1 :
# 1 2 3 4 4 6 7 11 13 

from sys import stdin

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    i  = 0
    j  = 0
    arr3 = []
    while i < n and j < m:
        if (arr1[i] >= arr2[j]):
            arr3.append(arr2[j])
            j = j +1
        else:
            arr3.append(arr1[i])
            i = i +1

    while i < n :
        arr3.append(arr1[i])
        i = i + 1

    while j < m:
        arr3.append(arr2[j])
        j = j + 1

    return arr3
