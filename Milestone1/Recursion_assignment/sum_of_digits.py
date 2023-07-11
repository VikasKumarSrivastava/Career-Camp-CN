# Write a recursive function that returns the sum of the digits of a given integer.
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def sum_digit(n):
    if n==0:
        return 0
    return n%10 + sum_digit(n//10)


n = int(input())
ans = sum_digit(n)
print(ans)
