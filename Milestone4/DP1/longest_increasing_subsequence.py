# Given an array with N elements, 
# you need to find the length of the longest subsequence in the given array such that
# all elements of the subsequence are sorted in strictly increasing order.
# Sample Input 1 :
# 6
# 5 4 11 1 16 8
# Sample Output 1 :
# 3
# Sample Output Explanation
# Length of longest subsequence is 3 i.e. (5,11,16) or (4,11,16).
# Sample Input 2 :
# 3
# 1 2 2
# Sample Output 2 :
# 2
# Recursive solution
# def lis(li,i,n):
#     if i==n:
#         return 0,0
#     including_max=1
#     for j in range(i+1,n):
#         if li[j]>=li[i]:
#             further_including_max=lis(li,j,n)[0]
#             including_max=max(including_max,1+further_including_max)
#     excluding_max=lis(li,i+1,n)[1]
#     overallMax=max(including_max,excluding_max)
#     return including_max,overallMax
# n=int(input())
# li=[int(ele) for ele in input().split()]
# ans=lis(li,0,n)[1]
# print(ans)
from sys import stdin

#TC O(N^2)
#SC O(N)
def lis(arr): 
    # Write your code here
    dp =[None for i in range(n)]
    dp[0]=1
    ans=1
    for i in range(1,n):
        max =1
        for j in range(i-1,-1,-1):
            if arr[j]<arr[i]:
                op=dp[j]+1
                if op>max:
                    max =op
        dp[i] = max
        if (max>ans):
            ans= max
    return ans
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))
