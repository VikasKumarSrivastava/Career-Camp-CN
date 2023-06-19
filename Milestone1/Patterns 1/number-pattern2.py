# Number Pattern 2
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
i =1
while i <= n:
    j=1
    while j<= i:
        if i ==1:
            print(1,end="")
        elif j==1 or j==i:
            print(i-1,end="")
        else:
            print(0,end="")
        j = j +1
    print()
    i = i +1
