def knapsack(W,val,wt,n,i):
    if i==n:
        return 0
    if wt[i]>W:
        ans=knapsack(W,val,wt,n,i+1)
    else:
        #inclusion of ith item
        ans1=val[i]+knapsack(W-wt[i],val,wt,n,i+1)
        #exclusion of ith item
        ans2=knapsack(W,val,wt,n,i+1)
        ans=max(ans1,ans2)
    return ans
val=[200,300,100]
wt=[20,25,30]
W=50
n=len(val)
ans=knapsack(W,val,wt,n,0)
print(ans)
