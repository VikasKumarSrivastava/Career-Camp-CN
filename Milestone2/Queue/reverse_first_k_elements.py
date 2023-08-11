# For a given queue containing all integer data, reverse the first K elements.
# You have been required to make the desired change in the input queue itself.
# The only line of output prints the updated order in which the queue elements are dequeued, all of them separated by a single space. 
# Sample Input 1:
# 5 3
# 1 2 3 4 5
# Sample Output 1:
# 3 2 1 4 5
# Sample Input 2:
# 7 7
# 3 4 2 5 6 7 8
# Sample Output 2:
# 8 7 6 5 2 4 3
from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    #Your code goes here
    stack = []
    n  = inputQueue.qsize()
    count=0

    if k==0 or k>n:
        return

    while(not inputQueue.empty()):
        temp = inputQueue.get()
        stack.append(temp)
        count+=1

        if count==k:
            break

    while (not isEmpty(stack)):
        temp = top(stack)
        stack.pop()
        inputQueue.put(temp)

    count = 0

    while(not inputQueue.empty() and n-k !=0):
        temp = inputQueue.get()
        count = count+1
        inputQueue.put(temp)

        if count == n-k:
            break

    return inputQueue

'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
