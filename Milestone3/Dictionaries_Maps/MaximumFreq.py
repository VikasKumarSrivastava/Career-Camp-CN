# You are given an array of integers that contain numbers in random order. 
# Write a program to find and return the number which occurs the maximum times in the given input.
# If two or more elements are having the maximum frequency, return the element which occurs in the array first.
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6 
# Sample Output 1 :
# 2
# Sample Input 2 :
# 3
# 1 4 5
# Sample Output 2 :
# 1
# Read input as sepcified in the question
# Print output as specified in the question
# TC=O(N)
# SC=O(N)
from sys import stdin

def maxFreq(arr):
    d={}
    for num in arr:
        d[num] = d.get(num,0) + 1
    ans = arr[0]
    for num in arr:
        if d[num] > d[ans]:
            ans=num
    return ans

def takeInput():
    n = int(stdin.readline().strip())
    if n==0:
        return list(),0
    
    arr = list(map(int,stdin.readline().strip().split()))
    return arr,n

arr,n= takeInput()
print(maxFreq(arr))
