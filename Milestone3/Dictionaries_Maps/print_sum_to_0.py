# Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
# Note: Array A can contain duplicate elements as well.
# Sample Input 1:
# 5
# 2 1 -2 2 3
# Sample Output 1:
# 2
# Explanation
# (2,-2) , (-2,2) will result in 0 , so the answer for the above problem is 2.

from sys import stdin
from math import factorial
#TC O(N)
#SC O(N)

def helperfun(n):
    ans=0
    if n!=1:
        ans=factorial(n)/ (factorial(2)*factorial(n-2))
    return int(ans)

def freq(l):
    map={}
    for num in l:
        map[num] = map.get(num,0) +1
    return map
def pairSum0(l,n):
    # Write your code here
    m= freq(l)
    count =0 
    for num in m:
        if num > 0 and -num in m:
            count = count+(m[num]*m[-num])
        
        if num==0:
            count+=helperfun(m[num])
    return count
                
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
