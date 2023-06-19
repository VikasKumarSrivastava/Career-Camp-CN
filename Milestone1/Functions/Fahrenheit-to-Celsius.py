# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
# Note: You don't have to write the main function or take input. It has already been taken care of. Just write the code that prints Fahrenheit to Celsius table in the function itself.
# Input Format :
# 3 integers - S, E and W respectively
# Sample Input 1:
# 0 
# 100 
# 20
# Sample Output 1:
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37
def printTable(start,end,step):
#Implement Your Code Here
	while start<= end:
		c = 5 * (start-32)/9
		print(start," ",int(c))
		start = start + step
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
