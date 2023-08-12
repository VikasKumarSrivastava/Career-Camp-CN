# You need to implement a class for Dequeue i.e. for double ended queue. In this queue, elements can be inserted and deleted from both the ends.
# You don't need to double the capacity.
# You need to implement the following functions -
# 1. constructor
# You need to create the appropriate constructor. Size for the queue passed is 10.
# 2. insertFront -
# This function takes an element as input and insert the element at the front of queue. 
# Insert the element only if queue is not full. And if queue is full, print -1 and return.
# 3. insertRear -
# This function takes an element as input and insert the element at the end of queue.
# Insert the element only if queue is not full. And if queue is full, print -1 and return.
# 4. deleteFront -
# This function removes an element from the front of queue. Print -1 if queue is empty.
# 5. deleteRear -
# This function removes an element from the end of queue. Print -1 if queue is empty.
# 6. getFront -
# Returns the element which is at front of the queue. Return -1 if queue is empty.
# 7. getRear -
# Returns the element which is at end of the queue. Return -1 if queue is empty.
# Sample Output 1:
# -1
# 64
# 99
# Explanation:
# The first choice code corresponds to getFront. Since the queue is empty, hence the output is -1. 
# The following input adds 49 at the top and the resultant queue becomes: 49.
# The following input adds 64 at the top and the resultant queue becomes: 64 -> 49
# The following input add 99 at the end and the resultant queue becomes: 64 -> 49 -> 99
# The following input corresponds to getFront. Hence the output is 64.
# The following input corresponds to getRear. Hence the output is 99.

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
class queue_using_array:
    def __init__(self):
        self.__arr =[]
        self.__count =0
    
    def insertRear(self,data):
        if self.__count ==10:
            return -1
        self.__arr.append(data)
        self.__count+=1
        return self.__arr

    def insertFront(self,data):
        if self.__count ==10:
            return -1
        self.__arr= [data]+self.__arr
        self.__count +=1
        return self.__arr
    
    def deleteRear(self):
        if self.__count ==0:
            print(-1)
        else:
            self.__arr.pop(-1)
            self.__count-=1
            return self.__arr
    
    def deleteFront(self):
        if self.__count ==0:
            print(-1)
        else:
            self.__arr.pop(0)
            self.__count-=1
            return self.__arr

    def getFront(self):
        if self.__count==0:
            return -1
        return self.__arr[0]

    def getRear(self):
        if self.__count ==0:
            return -1
        return self.__arr[-1]

inp = [int(x) for x in input().split(" ")]
i = 0
solve = queue_using_array()

while inp[i]!=-1:
    n = inp[i]
    i+=1
    if n==1:
        k = solve.insertFront(inp[i])
        if k ==-1:
            print(k)
        i+=1
    elif n==2:
        k= solve.insertRear(inp[i])
        if k == -1:
            print(-1)
        i+=1
    elif n ==3:
        solve.deleteFront()
    elif n==4:
        solve.deleteRear()
    elif n ==5:
        print(solve.getFront())
    elif n == 6:
        print(solve.getRear())
