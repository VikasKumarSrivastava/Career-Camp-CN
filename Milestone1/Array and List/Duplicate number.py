# Sample Input 1:
# 1
# 9
# 0 7 2 5 4 7 1 3 6
# Sample Output 1:
# 7

import sys

def duplicateNumber(arr, n) :
    #Your code goes here
    if n==1:
        return arr[0]
    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                if arr[i] == arr[j]:
                    return arr[i]
