# You are given with an array of integers and an integer K. 
# You have to find and print the count of all such pairs which have difference K.
# Note: Take absolute difference between the elements of the array.
#TC : O(n)
#SC : O(n)
# where n is the size of input array
# Sample Input 1 :
# 4 
# 5 1 2 4
# 3
# Sample Output 1 :
# 2
# Explanation
# (5,2) and (1,4) are the possible combinations as their absolute difference is 3.
# Sample Input 2 :
# 4
# 4 4 4 4 
# 0
# Sample Output 2 :
# 6

def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pairCount = 0
    m = {}

    for num in l:
        if num + k in m:
            pairCount+=m[num+k]
        if k!=0 and num-k in m:
            pairCount+=m[num-k]

        if num in m :
            m[num]+=1
        else:
            m[num] = 1
    return pairCount    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
