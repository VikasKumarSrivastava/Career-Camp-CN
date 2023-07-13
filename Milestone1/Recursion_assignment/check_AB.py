# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function 
# that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def check_AB(str):
    if len(str)==0:
        return True
    if (str[0] == 'a'):        
        if (len(str[1:])>1 and str[1:3] == 'bb'):
            return check_AB(str[3:])    
        else:
            return check_AB(str[1:])       
    else:
        return False

str = input()
if check_AB(str):
    print('true')
else:
    print('false')
