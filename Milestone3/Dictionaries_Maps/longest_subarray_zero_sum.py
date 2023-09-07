# Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
# Sample Input 1:
# 10 
#  95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output 1:
# 5
# Explanation:
# The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
#TC = O(n)
#SC = O(n)
# where n is the size of the input array
def subsetSum(l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n = len(l)
    sum = [0] * n
    sum[0] = l[0]
    m = {l[0]:0}
    start,end=-1,-2
    if sum[0] == 0:
        start,end =0,0
    
    for i in range(1,n):
        sum[i]=sum[i-1] + l[i]
        if sum[i] == 0:
            start,end=0,i
        elif sum[i] in m :
            if i-m[sum[i]] > end - start+1:
                start,end=m[sum[i]]+1,i
        else:
            m[sum[i]] = i
    return end - start +1
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
