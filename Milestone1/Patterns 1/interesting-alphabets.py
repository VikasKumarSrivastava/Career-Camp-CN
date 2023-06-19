# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = 1
while i <= n:
    p=0
    start_char = chr(ord('A')+n-i)
    j=1
    while j <=i:
        charP = chr(ord(start_char)+p)
        print(charP,end="")
        j=j+1
        p=p+1
    print()
    i = i+1
