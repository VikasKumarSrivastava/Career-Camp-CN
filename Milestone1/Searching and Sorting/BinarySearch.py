# You are given an integer array 'A' of size 'N', sorted in ascending order. You are also given an integer 'target'.
# Your task is to write a function to search for 'target' in the array 'A'. 
# If it exists, return its index in 0-based indexing. Otherwise, return -1.
# Note: You must write an algorithm whose time complexity is O(logN).
# Example:
# Input: ‘N’ = 7 ‘target’ = 3
# ‘A’ = [1, 3, 7, 9, 11, 12, 45]
# Output: 1
# Explanation: For A = [1, 3, 7, 9, 11, 12, 45],
# The index of element '3' is 1.
# Hence, the answer is '1'.
def search(nums: [int], target: int):
    # Your code goes here
    l = 0
    h = len(nums)-1
    while l <= h:
        mid = (l + h)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            h = mid - 1
        else:
            l = mid + 1        
    return -1
