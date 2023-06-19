# Sum of Even Numbers
# Send Feedback
# Given a number N, print sum of all even numbers from 1 to N.
# Input Format :
# Integer N
# Output Format :
# Required Sum 
# Sample Input 1 :
#  6
# Sample Output 1 :
# 12

n=int(input())
sum=0
i=1

while i <= n:
    if i%2 ==0:
        sum = sum+i
    i=i+1
print(sum)
