# You have been given two stacks that can store integers as the data. Out of the two given stacks, 
# one is populated and the other one is empty. 
# You are required to write a function that reverses the populated stack using the one which is empty.
# Sample Input 1:
# 6
# 1 2 3 4 5 10
# Note:
# Here, 10 is at the top of the stack.
# Sample Output 1:
# 1 2 3 4 5 10
# Note:
# Here, 1 is at the top of the stack.
# Sample Input 2:
# 5
# 2 8 15 1 10
# Sample Output 2:
# 2 8 15 1 10



from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	#Your code goes here
	if len(inputStack) ==0:
		return
	lastelement = inputStack.pop()

	reverseStack(inputStack,extraStack)

	while not isEmpty(inputStack):
		top = inputStack.pop()
		extraStack.append(top)
	
	inputStack.append(lastelement)

	while not isEmpty(extraStack):
		top = extraStack.pop()
		inputStack.append(top)


def isEmpty(stack):
	return len(stack) == 0


'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
