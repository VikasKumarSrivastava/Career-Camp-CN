# Reverse of a number
# Send Feedback
# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
#Write Your Code Here
n = int(input())
ans =0
while n!=0:
    d = n%10
    ans= ans*10 + d
    n = n//10   
print(ans)
