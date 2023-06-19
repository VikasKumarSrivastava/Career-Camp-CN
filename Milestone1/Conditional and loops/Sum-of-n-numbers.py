# Sum of n numbers
# Given an integer n, find and print the sum of numbers from 1 to n.
# Note
# Use while loop only.
# Input Format :
# Integer n
# Output Format :
# Sum of numbers
# Sample Input :
# 10
# Sample Output :
# 55
n=int(input())
sum=0
i=0

while i <= n:
    sum = sum+i
    i=i+1
print(sum)
