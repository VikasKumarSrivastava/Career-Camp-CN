# You have made a smartphone app and want to set its subscription price such that the profit earned is maximised. There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.
# You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit that you can earn.
# Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you can earn is :
#  m * x
# where m is total number of subscribers whose budget is greater than or equal to x.
# Input format :
# Line 1 : N (No. of subscribers)
# Line 2 : Budget of subscribers (separated by space)
# Output Format :
#  Maximum profit

def maximumProfit(arr):
	#Implement Your Function here
	arr.sort()
	ans=-10000000000
	b=len(arr)
	for i in range(0,b):
		ans=max(ans,arr[i]*(b-i));
	return ans


n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
