# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.
# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1

from sys import stdin

def findUnique(arr, n) :
    #Your code goes here
    d={}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] +=1
        else:
            d[arr[i]] =1
    
    for i in d.keys():
        if d[i]==1:
            return i
