# You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.
# Sample Input 1 :
# 1
# 9 2 3 3 2 9 -1
# Sample Output 1 :
# true
# Sample Input 2 :
# 2
# 0 2 3 2 5 -1
# -1
# Sample Output 2 :
# false
# true
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reversedLL(head):
    curr=head
    prev = None
    temp= None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def isPalindrome(head) :
    #Your code goes here
    if head is None or head.next is None:
        return True

    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    secondHead = slow.next
    slow.next = None
    secondHead = reversedLL(secondHead)

    firstSublist = secondHead
    secondSublist = head

    while firstSublist is not None:
        if firstSublist.data != secondSublist.data:
            return False
        firstSublist = firstSublist.next
        secondSublist = secondSublist.next

    return True


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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1
