# Print the following pattern for the given number of rows.
# Note: N is always odd.
# ..*
# .***
# *****
# .***
# ..*

# Pattern for N = 5
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
first_half  = n//2 +1
second_half = n//2
i= 1
while i <= first_half :
    space =1
    while space <= first_half-i:
        print(' ',end='')
        space = space +1
    j=1
    while j <= 2*i - 1:
        print('*',end ='')
        j=j+1
    print()
    i =i +1

i = second_half
while i  >= 1:
    space =1
    while space <= (second_half - i + 1):
        print(' ',end='')
        space = space +1
    j=1
    while j <= 2*i - 1:
        print('*',end ='')
        j=j+1
    print()
    i =i -1
