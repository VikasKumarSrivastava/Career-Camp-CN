# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.
# Sample Input 1:
# aabccbaa
# a
# Sample Output 1:
# bccb
from sys import stdin
def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	ans =""
	for i in string:
		if i ==ch:
			continue
		else:
			ans = ans + i
	return ans
