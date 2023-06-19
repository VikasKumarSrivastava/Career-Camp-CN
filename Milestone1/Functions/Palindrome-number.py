# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
# Sample Input 1 :
# 121
# Sample Output 1 :
# true
n=int(input())  
# taking n as a input 
## write your code !!

num= n
ans = 0 
while num != 0:
    digit = num%10
    ans = ans*10 + digit
    num = num//10

if ans == n:
    print('true')
else:
    print('false')
