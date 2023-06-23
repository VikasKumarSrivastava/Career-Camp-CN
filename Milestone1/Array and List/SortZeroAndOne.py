# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list.
# Think of a solution which scans the array/list only once and don't require use of an extra array/list.
# Sample Input 1:
# 1
# 7
# 0 1 1 0 1 0 1
# Sample Output 1:
# 0 0 0 1 1 1 1
def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    #Way 1
    # count_zero =0
    # count_one=0
    # for i in range(0,n):
    #     if arr[i] == 0:
    #         count_zero = count_zero +1
    #     if arr[i] == 1:
    #         count_one = count_one + 1
    # len_zero = count_zero
    # for j in range(0,count_zero+1):
    #     arr.insert(j,0)
    
    # for k in range(count_zero,n):
    #     arr.insert(k,1)
    #Way 2
    low = 0
    high = n-1
    while low <= high:
        if arr[low] ==  0:
            low =low+1
        elif arr[high] ==1:
            high = high -1
        else:
            arr[low],arr[high] = arr[high],arr[low]
