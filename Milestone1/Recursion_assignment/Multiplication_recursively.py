# Given two integers M & N, calculate and return their multiplication using recursion. 
# You can only use subtraction and addition for your calculation. No other operators are allowed.
# Input format :
# Line 1 : Integer M
# Line 2 : Integer N
# Output format :
# M x N
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def multi(m, n):
    if n==1 or m==0:
        return m
    return m + multi(n-1,m)
m = int(input())
n = int(input())
if m < 0 or n< 0:
        print()
else:
    print(multi(m,n))
