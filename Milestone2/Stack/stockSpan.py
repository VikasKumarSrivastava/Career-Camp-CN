# Afzal has been working with an organization called 'Money Traders' for the past few years. The organization is into the money trading business. 
# His manager assigned him a task. For a given array/list of stock's prices for N days, find the stock's span for each day.
# The span of the stock's price today is defined as the maximum number of consecutive days(starting from today and going backwards) 
# for which the price of the stock was less than today's price.
# For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85], then the stock spans will be [1, 1, 1, 2, 1, 4, 6].
# Explanation:
# On the sixth day when the price of the stock was 75, the span came out to be 4, because the last 4 prices(including the current price of 75) 
# were less than the current or the sixth day's price.

# Similarly, we can deduce the remaining results.
# Afzal has to return an array/list of spans corresponding to each day's stock's price. Help him to achieve the task.
# Sample Input 1:
# 4
# 10 10 10 10
# Sample Output 1:
# 1 1 1 1 
# Sample Input 2:
# 8
# 60 70 80 100 90 75 80 120
# Sample Output 2:
# 1 2 3 4 1 1 2 8 
from sys import stdin

def top(stack):
	return stack[len(stack)-1]

def isEmpty(stack):
	return len(stack)==0

def stockSpan(price, n) :
	#TC -> O(n^2) --> TLE
	#Your code goes here
	# stack =[]
	# spans=[]
	# for i in range(n):
	# 	stack.append(price[i])
	# 	curr = top(stack) 
	# 	k=0
	# 	count = 1
	# 	while k<=i:		
	# 		if curr > price[k]:
	# 			count=count+1				
	# 		elif curr == price[k]:
	# 			count = count
	# 		else:
	# 			count = 1
	# 		k+=1
	# 	spans.append(count)
	# return spans

	# solution2
	#TC O(n)
	stack =[]
	spans=[-1]*n
	stack.append(0)
	spans[0] = 1
	for i in range(1,n):
		while (not isEmpty(stack)) and (price[top(stack)] < price[i]):
			stack.pop()
		if isEmpty(stack) :
			spans[i] =i+1
		else:
			spans[i] = i - top(stack)
		stack.append(i)

	return spans
			
'''-------------- Utility Functions --------------'''

def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
