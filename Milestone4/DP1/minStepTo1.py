# Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. 
# You can perform any one of the following 3 steps:
# 1.) Subtract 1 from it. (n = n - ­1) ,
# 2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
# 3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  
# Sample Input 1 :
# 4
# Sample Output 1 :
# 2 
# Explanation of Sample Output 1 :
# For n = 4
# Step 1 :  n = 4 / 2  = 2
# Step 2 : n = 2 / 2  =  1 
# Sample Input 2 :
# 7
# Sample Output 2 :
# 3
# Explanation of Sample Output 2 :
# For n = 7
# Step 1 :  n = 7 ­- 1 = 6
# Step 2 : n = 6  / 3 = 2 
# Step 3 : n = 2 / 2 = 1  
from sys import stdin
from sys import maxsize as MAX_VALUE

def countMinStepsToOne(n) :
    dp=[0]*(n+1)
    dp[1]=0
    for i in range(2,n+1):
        op1=1e9
        op2=1e9
        op3=1e9
        op1 = dp[i-1]
        if i%2==0:
            op2=dp[i//2]
        if i%3==0:
            op3=dp[i//3]

        dp[i]= min(op1,op2,op3)+1
    return dp[n]


#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))
