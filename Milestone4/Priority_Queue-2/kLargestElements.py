# You are given with an integer k and an array of integers that contain numbers in random order.
# Write a program to find k largest numbers from given array. You need to save them in an array and return it.
# Time complexity should be O(nlogk) and space complexity should be not more than O(k).
# Sample Input :
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6 
# 4
# Sample Output :
# 12
# 16
# 20
# 25
import heapq
def kLargest(lst, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    heapq._heapify_max(lst)
    ans=[]
    for i in range(0,k):
       ans.append( heapq._heappop_max(lst))
    return ans

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
