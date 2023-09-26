# An integer matrix of size (M x N) has been given. Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
# From a cell (i, j), you can move in three directions:
# 1. ((i + 1),  j) which is, "down"
# 2. (i, (j + 1)) which is, "to the right"
# 3. ((i+1), (j+1)) which is, "to the diagonal"
# The cost of a path is defined as the sum of each cell's values through which the route passes.
# Constraints :
# 1 <= M <= 10 ^ 2
# 1 <= N <=  10 ^ 2

# Time Limit: 1 sec
# Sample Input 1 :
# 3 4
# 3 4 1 2
# 2 1 8 9
# 4 7 8 1
# Sample Output 1 :
# 13
# Sample Input 2 :
# 3 4
# 10 6 9 0
# -23 8 9 90
# -200 0 89 200
# Sample Output 2 :
# 76
# Sample Input 3 :
# 5 6
# 9 6 0 12 90 1
# 2 7 8 5 78 6
# 1 6 0 5 10 -4 
# 9 6 2 -10 7 4
# 10 -2 0 5 5 7
# Sample Output 3 :
# 18

from sys import stdin
MAX_VALUE = 2147483647

def minCostPath(input, mRows, nCols) :
	#Your code goes here
    dp=[[MAX_VALUE for j in range(nCols+1)]for i in range(mRows+1)]

    for i in range(mRows-1,-1,-1):
        for j in range(nCols-1,-1,-1):
            if i==mRows-1 and j ==nCols-1:
                dp[i][j] = input[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2= dp[i][j+1]
                ans3= dp[i+1][j+1]
                dp[i][j] = input[i][j]+ min(ans1,ans2,ans3)
    return dp[0][0]

#taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))
