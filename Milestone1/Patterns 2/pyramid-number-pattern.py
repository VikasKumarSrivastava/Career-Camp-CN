# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234
# Input format : N (Total no. of rows)

# Output format : Pattern in N lines
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i =1
while i <= n:
    spaces =1
    while spaces <= n -i:
        print(' ',end='')
        spaces =spaces +1
    k = i
    while k >= 1:
        print(k,end='')
        k = k -1
    l=2
    while l <= i and i >= 2:
        print(l,end='')
        l = l +1
    print()
    i=i+1
