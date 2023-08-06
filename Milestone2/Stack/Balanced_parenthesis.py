from sys import stdin

def isBalanced(expression) :
	#Your code goes here
	s = []
	for e in expression:
		if e=='(':
			s.append('(')
		elif e==')':
			if len(s) !=0 and s[-1] =='(':
				s.pop()
			else:
				return False
	if len(s) == 0:
		return True
	else:
		return False

#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
