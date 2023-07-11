# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# using recursion.
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def geometric_sum(n):
    if n==0:    
        # return float('%.5f'%1)
        return 1
    return  (2**-n)+ geometric_sum(n-1)

n = int(input())
ans =geometric_sum(n)
print("%.5f"%ans)
