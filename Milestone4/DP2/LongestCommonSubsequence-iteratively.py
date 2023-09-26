# Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.
# For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order
# as they are present in 'str,' but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K.
# Example :
# Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.
# ample Input 1 :
# adebc
# dcadb
# Sample Output 1 :
# 3
# Explanation of the Sample Output 1 :
# Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 
# Sample Input 2 :
# ab
# defg
# Sample Output 2 :
# 0
# Explanation of the Sample Output 2 :
# The only subsequence that is common to both the given strings is an empty string("") of length 0.
#TC  O(n*m)
#SC  O(n+m)
from sys import stdin

def lcs(s, t) :
	#Your code goes here
	n = len(s)
	m = len(t)

	dp=[[0 for j in range(m+1)] for i in range(n+1)]

	for i in range(n-1,-1,-1):
		for j in range(m-1,-1,-1):
			if s[i]==t[j]:
				dp[i][j]=1+dp[i+1][j+1]
			else:
				dp[i][j]=max(dp[i+1][j],dp[i][j+1])
	return dp[0][0]


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
