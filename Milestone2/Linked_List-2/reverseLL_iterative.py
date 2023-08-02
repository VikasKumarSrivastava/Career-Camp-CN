# Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# Sample Output 1 :
# 8 7 6 5 4 3 2 1
from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
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


# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


def reverse(head):
    # Write your code here
    if head is None:
        return head
    curr = head
    prev = None
    temp = None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    
    ans=reverse(head)
    printLinkedList(ans)

    t -= 1 

