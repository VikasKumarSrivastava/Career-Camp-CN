# For a given string(str), remove all the consecutive duplicate characters.
# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"
# Sample Input 1:
# aabccbaa
# Sample Output 1:
# abcba
# Sample Input 2:
# xxyyzxx
# Sample Output 2:
# xyzx
from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
	if(len(string)==1):
		return string
	ansString = string[0]
	i = 1
	j = 0 # track elements in ansString
	while i < len(string):
		if string[i-1] == string[i]:
			if len(ansString)== 0:		
				ansString= ansString+string[i]
				j= j+1
			elif(string[i] != ansString[j-1]):
				ansString= ansString+string[i]
				j=j+1

		else:
			ansString= ansString+string[i]

		i = i +1
	return ansString
