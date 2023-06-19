# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
#     F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1


# Input Format :
# Integer N
# Output Format :
# true or false

def checkMember(n):
#Implement Your Code Here
    if n == 0 or n==1:
        return True
    x = 0
    y =1
    sum  = x + y
    while sum <= n:
        if(sum == n ):
            return True
        x = y
        y= sum
        sum = x + y
        
    return False


n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
