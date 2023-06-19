# Print the following pattern for a given n.
# For eg. N = 6
# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i=1
while i <= n:
    j=1
    while j <= n:
        space =1
        while space <= i-1:
            print(' ',end='')
            space = space +1
        p=i
        while p <= n:
            print(p,end='')
            p = p+1
        j = j + 1
        print()
        i = i+1

n1 =  n -1
i =1
while i <= n1:
    j = i
    p=1
    while j <= i:
        space = 1
        while space <= n1-i:
            print(' ',end='')
            p = p + 1
            space =space + 1
        while p <= n:
            print(p,end='')
            p = p  + 1
        j = j + 1
    print()
    i= i+1
