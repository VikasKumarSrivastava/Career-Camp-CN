# You have been given a singly linked list of integers where the elements are sorted in ascending order. 
# Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.
# Sample Input 1 :
# 1
# 1 2 3 3 3 3 4 4 4 5 5 7 -1
# Sample Output 1 :
# 1 2 3 4 5 7 
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def removeDuplicates(head) :
    #Your code goes here
    if head is None:
        return head
    currhead = head
    while currhead.next is not None:
        if currhead.data == currhead.next.data:
            currhead.next = currhead.next.next
        else:
            currhead = currhead.next
    return head


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1
