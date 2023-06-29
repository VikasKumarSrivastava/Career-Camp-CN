# Aadil has been provided with a sentence in the form of a string as a function parameter. 
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed. 
# A word is a combination of characters without any spaces.
# Sample Input 1:
# Welcome to Coding Ninjas
# Sample Output 1:
# emocleW ot gnidoC sajniN

from sys import stdin
def reverseEachWord(string) :
	# Your code goes here
	#string to array
	li = string.split()
  
	rev_li=[]
	ans=" "
	j = 0
  
	for i in li:
		rev_li.insert(j,i[::-1])
		j=j+1
    
	#list to string
	return(ans.join(rev_li))

