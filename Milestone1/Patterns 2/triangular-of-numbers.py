# Print the following pattern for the given number of rows.
# Pattern for N = 4
# ...1
# ..232
# .34543
# 4567654
# The dots represent spaces.
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n =int (input())
i = 1
while i <= n:
    j =1
    while j <= n-i:
        print(" ",end="")
        j=j+1
    m=0
    while j<=n:
        print(i+m,end="")
        j=j+1
        m=m+1
    k=1
    l=2
    while k <= i-1:
        print(2*i-l,end="")
        k=k+1
        l=l+1
    print()
    i = i+1
