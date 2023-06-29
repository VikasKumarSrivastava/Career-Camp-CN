# Write a program to do basic string compression. 
# For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(input) :
	# Write your code here.
	res=""
	cnt = 1

	for i in range(1, len(input)):
		if input[i] ==input [i-1]:
			cnt = cnt + 1
		else:
			res = res + input[i-1]
			if cnt > 1:
				res += str(cnt)
			cnt  = 1
	res = res + input[-1]
	if cnt>1:
		res+=str(cnt)
	return res
