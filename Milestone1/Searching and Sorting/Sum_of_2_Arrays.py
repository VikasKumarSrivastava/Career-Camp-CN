# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. 
# Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index).
# The idea here is to represent each array/list as an integer in itself of digits N and M.
# You need to find the sum of both the input arrays/list treating them as two integers and 
# put the result in another array/list i.e. output array/list will also contain only single digit at every index.
# Sample Input 1:
# 1
# 3
# 6 2 4
# 3
# 7 5 6
# Sample Output 1:
# 1 3 8 0


from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    #Your code goes here
    i = n-1
    j = m-1
    carry = 0
    l = max(n, m)+1
    while i >= 0 and j >= 0:
        num = arr1[i]+arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
        j = j-1
    while i >= 0:
        num = arr1[i]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        i = i-1
    while j >= 0:
        num = arr2[j]+carry
        s = num % 10
        carry = num//10
        output[l-1] = s
        l = l-1
        j = j-1
    if carry != 0:
        output[0] = carry
