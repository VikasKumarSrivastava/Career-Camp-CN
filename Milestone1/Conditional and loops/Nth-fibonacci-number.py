# Nth Fibonacci Number
# Send Feedback
# Write a program to find the Nth Fibonacci number using loops.
# Input Format :
# The first line of each test case contains a real number ‘N’.
# Output Format :
# For each test case, print its equivalent Fibonacci number.
# Constraints:
# 1 <= N <= 10000     
# Where ‘N’ represents the number for which we have to find its equivalent Fibonacci number.

# Time Limit: 1 second
# Sample Input 1:
# 6
# Sample Output 1:
# 8
# Explanation
# The Fibonacci sequence starts with two numbers first number is 1 and second number is also 1. The subsequent numbers are found by adding the two preceding numbers. 
# Therefore, the first six Fibonacci numbers are: 1, 1, 2, 3, 5, 8 . 
# Hence, the 6th Fibonacci number is 8.
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
n1 = 1
n2 = 1 
if( n==1):
    print(n1)
elif(n==2):
    print(n2)
else:
    i = 3
    ans =0
    while i <= n:
        ans = n1+n2
        n1=n2
        n2=ans
        i= i+1
    print(ans)

