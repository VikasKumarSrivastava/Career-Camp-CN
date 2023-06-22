
# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.
# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1
import sys

def findUnique(arr, n) :
    #Your code goes here
    if n == 1:
        return arr[0]
    for i in range(0,len(arr)):       
        for j in range (0,len(arr)):
            if i != j:
                if arr[i] == arr[j]:
                    break
        if j == (len(arr) - 1):
            return arr[i]  
                
                
                
