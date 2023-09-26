import sys


def minCost(cost,i,j,n,m,dp):
    if i==n-1 and j==m-1:
        return cost[i][j]
    if i>=n or j>=m:
        return sys.maxsize
    
    if dp[i+1][j]==sys.maxsize:
        ans1=minCost(cost,i+1,j,n,m,dp)
        dp[i+1][j]=ans1
    else:
        ans1=dp[i+1][j]
        
    if dp[i][j+1]==sys.maxsize:
        ans2=minCost(cost,i,j+1,n,m,dp)
        dp[i][j+1]=ans2
    else:
        ans2=dp[i][j+1]
    if dp[i+1][j+1]==sys.maxsize:
        ans3=minCost(cost,i+1,j+1,n,m,dp)
        dp[i+1][j+1]=ans3
    else:
        ans3=dp[i+1][j+1]
    ans = cost[i][j]+min(ans1,ans2,ans3)
    return ans


cost=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n=4
m=3
dp=[[sys.maxsize for j in range(m+1)]for i in range(n+1)]
ans = minCost(cost,0,0,4,3,dp)
print(ans)
