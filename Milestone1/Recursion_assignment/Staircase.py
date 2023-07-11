# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def jump(n):
    if n==0 or n==1:
        return 1
    elif n ==2:
        return 2
    else:
        return jump(n-1)+jump(n-2)+jump(n-3)

n = int(input())
print(jump(n))
