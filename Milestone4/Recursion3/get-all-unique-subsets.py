# You are given an sorted integer array of size 'n'.
# Your task is to find and return all the unique subsets of the input array.
# Subsets are arrays of length varying from 0 to 'n', that contain elements of the array. But the order of elements should remain the same as in the input array.
#   Sample Input 1 :
# 3
# 12 15 20
# Sample Output 1 :
# [] (this represents an empty array)
# 12 
# 12 15 
# 12 15 20 
# 12 20 
# 15 
# 15 20 
# 20 
# Explanation Of Sample Input 1 :
# Since there are no repeated numbers, 8 subsets are generated.
# Sample Input 2 :
# 3
# 1 1 2
# Sample Output 2 :
# []    
# 1 
# 1 1 
# 1 1 2 
# 1 2 
# 2 
# Explanation Of Sample Input 2 :
# Since there are repeated numbers, the total number of unique subsets is 6.
# Expected Time Complexity :
# The expected time complexity is O(k * 2^n), where n is the size of the array and 'k' is the average size of a subset.
# Expected Space Complexity :
# The expected time complexity is O(k * 2^n), where n is the size of the array and 'k' is the average size of a subset.
# Constraints :
# 1 <= n <= 15
# 1 <= arr[i] <= 100

# Time Limit: 1 sec
from math import *
from collections import *
from sys import *
from os import *
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # write the code  logic here !!! 
        ans=[]
        res=set()
        def fun(index: int,ds: List[int]):
            if index == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(nums[index])
            fun(index+1,ds)
            ds.pop()
            fun(index+1,ds)
        fun(0,[])
        for it in res:
            ans.append(list(it))
        return ans

if __name__ == "__main__":
    n= int (input())
    nums=list(map(int, input().split()))  
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
