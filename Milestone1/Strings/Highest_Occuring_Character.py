# For a given a string(str), find and return the highest occurring character.
# Example:
# Input String: "abcdeapapqarr"
# Expected Output: 'a'
# Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.
# Sample Input 1:
# abdefgbabfba
# Sample Output 1:
# b
# Sample Input 2:
# xy
# Sample Output 2:
# x
from sys import stdin

def highestOccuringChar(string) :
	#Your code goes here

	freq={}

	for i in string:
		if i in freq:
			freq[i] +=1
		else:
			freq[i] = 1
	ans = -2147483648
	ans_alpha=[]
	for j in string:
		if freq[j] > ans:
			ans = freq[j]
			ans_alpha.insert(0,j)

	return ans_alpha[0]
