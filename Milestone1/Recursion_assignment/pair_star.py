# Given a string S, 
# compute recursively a new string where identical chars that are adjacent 
# in the original string are separated from each other by a "*".
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a
  
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def pairStar(str,output,i=0):
    #Append current character
    output = output+ str[i]
    # if we reached last character
    if i == len(str)-1:
        print(output)
        return
    # If next character is same,
    # append '*'
    if str[i] ==str[i+1]:
        output = output +"*"
    pairStar(str,output,i+1)

str = input()
output=""
pairStar(str,output)
