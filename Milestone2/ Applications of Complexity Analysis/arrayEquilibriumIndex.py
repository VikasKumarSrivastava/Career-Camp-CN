# For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
# Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] 
# is equal to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the index 'i' is not included in either part.
# If more than one equilibrium indices are present, 
# then the index appearing first in left to right fashion should be returned. Negative one(-1) if no such index is present.
# Sample Input 1 :
# 1
# 5
# 1 4 9 3 2
# Sample Output 1 :
# 2
from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    #Your code goes here
    l_sum = 0
    r_sum = 0    
    n = len(arr)
    if n ==1:
        return 0
    j = 0
    total_sum = 0
    while j < n:
        total_sum = total_sum + arr[j]
        j = j + 1
    i=0
    while i < n:
        if i > 0:
            l_ele = arr[i-1]
        else:
            l_ele = 0
        curr_ele = arr[i]
        l_sum = l_sum+l_ele
        r_sum = total_sum - curr_ele - l_sum
        if l_sum == r_sum:
            return i
        i = i+1
    return -1

#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1
