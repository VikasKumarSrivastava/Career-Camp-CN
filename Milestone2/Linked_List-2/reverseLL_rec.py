# Given a singly linked list of integers, reverse it using recursion and return the head to the modified list.
# You have to do this in O(N) time complexity where N is the size of the linked list.
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# Sample Output 1 :
# 8 7 6 5 4 3 2 1
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 8)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def solve(head):
    if head is None or head.next is None:
        return head,head
    newHead ,newTail= solve(head.next)
    newTail.next = head
    head.next = None
    return newHead,head

def reverseLinkedListRec(head) :
	#Your code goes here
    head1 , tail = solve(head)
    return head1

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

def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
