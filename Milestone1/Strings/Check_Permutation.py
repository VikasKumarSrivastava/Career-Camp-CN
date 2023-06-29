# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.
# Permutations of each other
# Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

# Example: 
# str1= "sinrtg" 
# str2 = "string"

# The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.
# Sample Input 1:
# abcde
# baedc
# Sample Output 1:
# true
from sys import stdin
def isPermutation(string1, string2) :
	#Your code goes here
    if len(string1) != len(string2):
        return False
    ## create frequency array
    freq ={}
    for item in string1:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for item2 in string2:
        if item2 in freq:
            freq[item2] -=1
        else:
            freq[item2] =1
    for i in string1:
        if freq[i] != 0:
            return False
    return True
