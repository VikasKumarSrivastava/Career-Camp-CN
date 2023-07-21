# You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
# Note:
# Given array/list can contain duplicate elements. 
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an integer 'num'.
# Output format :
# For each test case, print the total number of pairs present in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^4
# 0 <= num <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 9
# 1 3 6 2 5 4 3 2 4
# 7
from sys import stdin

def pairSum(arr, n, num) :
	#Your code goes here
    # if n ==0:
    #     return 0
    # count= 0
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         if arr[i] + arr[j] == num:
    #             count= count + 1
    # return count
    d = {}
    count = 0
    for i in range(n):
        if num - arr[i] in d:
            count += d[num - arr[i]]
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    return count
