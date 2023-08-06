# Implement a Stack Data Structure specifically to store integer data using a Singly Linked List.
# The data members should be private.
# You need to implement the following public functions :
# 1. Constructor:
# It initialises the data members as required.
# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.
# 3. pop() :
# It pops the element from the top of the stack and in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.
# 4. top :
# It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.
# 5. size() :
# It returns the size of the stack at any given instance of time.
# 6. isEmpty() :
# It returns a boolean value indicating whether the stack is empty or not.
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    #Define data members and __init__()
    def __init__(self):
        self.head = None
        self.count =0
    def getSize(self) :
        #Implement the getSize() function
        return self.count

    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.getSize() == 0

    def push(self, data) :
        #Implement the push(element) function
        newNode= Node(data)
        newNode.next = self.head
        self.head = newNode
        self.count+=1

    def pop(self) :
        #Implement the pop() function
        if self.isEmpty():
            return -1
        temp = self.head.data
        self.head = self.head.next
        self.count-=1
        return temp

    def top(self) :
        #Implement the top() function
        if self.isEmpty():
            return -1
        return self.head.data
        




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
