# You have been given a singly linked list of integers along with an integer 'N'.
# Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.
# Sample Input 1 :
# 2
# 1 2 3 4 5 -1
# 3
# 10 20 30 40 50 60 -1
# 5
# Sample Output 1 :
# 3 4 5 1 2
# 20 30 40 50 60 10
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def appendLastNToFirst(head, n) :
    #Your code goes here
    if head is None:
        return
    tail = head
    count = 1
    while tail.next is not None:
        count +=1
        tail =tail.next
    i  = count - n
    curr = head
    for j in range(i-1):
        curr = curr.next
    tail.next = head
    head = curr.next
    curr.next = None
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
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 
