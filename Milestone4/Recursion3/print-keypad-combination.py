# Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
#   Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def getString(n):
    if n==2:
        return 'abc'
    if n==3:
        return 'def'
    if n==4:
        return 'ghi'
    if n==5:
        return 'jkl'
    if n==6:
        return 'mno'
    if n==7:
        return 'pqrs'
    if n==8:
        return 'tuv'
    if n==9:
        return 'wxyz'
    return ' '

def printKeypad(n,output):
    if n == 0:
        print(output)
        return
    smallInteger = n//10
    lastDigit = n%10

    optionForLastDigit = getString(lastDigit)

    for c in optionForLastDigit:
        newOutput = c+ output
        printKeypad(smallInteger,newOutput)


n = int(input())
printKeypad(n,'')
