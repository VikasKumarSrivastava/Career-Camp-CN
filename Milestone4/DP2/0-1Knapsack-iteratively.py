# A thief robbing a store can carry a maximal weight of W into his knapsack.
# There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the maximum value V, that the thief can steal?
# Constraints :
# 1 <= N <= 20
# 1<= Wi <= 100
# 1 <= Vi <= 100

# Time Limit: 1 sec
# Sample Input 1 :
# 4
# 1 2 4 5
# 5 4 8 6
# 5
# Sample Output 1 :
# 13
# Sample Input 2 :
# 5
# 12 7 11 8 9
# 24 13 23 15 16
# 26
# Sample Output 2 :
# 51

from sys import stdin

def knapsack(weights, values, n, maxWeight) :
	#Your code goes here
    dp=[[0 for j in range(maxWeight+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,maxWeight+1):
            if j < weights[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = values[i-1]+dp[i-1][j-weights[i-1]]
                ans2 = dp[i-1][j]

                ans = max(ans1,ans2)
            
            dp[i][j] = ans
    return dp[n][maxWeight]

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight))
