# Given an array of integers, check whether it represents max-heap or not. 
# Return true if the given array represents max-heap, else return false.
# Sample Input 1:
# 8
# 42 20 18 6 14 11 9 4
# Sample Output 1:
# true
#TC O(N)
#SC O(1) ; where N is the size of input array
def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n = len(lst)
    for i in range(n):
        leftInd = 2*i+1
        rightInd = 2*i+2
        if leftInd <n and lst[leftInd]>lst[i]:
            return False
        if rightInd < n and lst[rightInd]>lst[i]:
            return False
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
