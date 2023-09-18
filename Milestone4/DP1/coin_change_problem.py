def minNumberOfCoinsForChangeHelper(n,denoms,dp):
    if n == 0:
        return 0
    if n < 0:
        return 99999
    if dp[n] != -1:
        return dp[n]
    mini = 99999
    for i in range(0,len(denoms)):
        ans = minNumberOfCoinsForChangeHelper(n-denoms[i],denoms,dp)
        if ans != 99999:
            mini = min(1+ans,mini)
    dp[n] = mini
    return dp[n]
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    dp=[-1]*(n+1)
    ans = minNumberOfCoinsForChangeHelper(n,denoms,dp)
    if ans == 99999:
        return -1
    return ans
