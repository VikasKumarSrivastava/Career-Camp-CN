# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). 
# Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these, 
# there is a single integer value that is present twice. You need to find and return that duplicate number present in the array.
# Sample Input 1:
# 1
# 9
# 0 7 2 5 4 7 1 3 6
# Sample Output 1:
# 7

from sys import stdin
def findDuplicate(arr, n) :
    #Your code goes here
    d={}

    for i in range(n):
        if arr[i] in d:
            if d[arr[i]] ==1:
                return arr[i] 
        else:
            d[arr[i]] =1
        
