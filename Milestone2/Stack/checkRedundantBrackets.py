# For a given expression in the form of a string, find if there exist any redundant brackets or not. 
# It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
# A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.
# Example:
# Expression: (a+b)+c
# Since there are no needless brackets, hence, the output must be 'false'.

# Expression: ((a+b))
# The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.
# Sample Input 1:
# a+(b)+c 
# Sample Output 1:
# true
# Explanation:
# The expression can be reduced to a+b+c. Hence, the brackets are redundant.
# Sample Input 2:
# (a+b)
# Sample Output 2:
# false
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
	stack =[]
	for i in range(len(expression)):
		if expression[i] == '(' or find(expression[i]):
			stack.append(expression[i])		
		elif expression[i]==')':
			operatorPresent = False

			while not isEmpty(stack) and topElement(stack) !='(':
				stack.pop()
				operatorPresent=True

			if not operatorPresent:
				return True
			
			if not isEmpty(stack):
				stack.pop()
	return False

	
def find(ch):
	if ch=='+' or ch=='-' or ch =='*' or ch=='/':
		return True
	else:
		return False
def isEmpty(st):
	return len(st)==0

def topElement(st):
	return st[len(st)-1]

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
