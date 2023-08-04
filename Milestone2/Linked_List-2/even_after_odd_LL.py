# For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.
# Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Sample Input 1 :
# 1
# 1 4 5 2 -1
# Sample Output 1 :
# 1 5 4 2 
# Sample Input 2 :
# 2
# 1 11 3 6 8 0 9 -1
# 10 20 30 40 -1
# Sample Output 2 :
# 1 11 3 9 6 8 0
# 10 20 30 40
from sys import stdin
#TC O(N)
#SC O(1)
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    if head is None:
        return head
    temp = head
    odd_head = None
    odd_tail=None
    even_head =None
    even_tail = None

    while temp is not None:
        if temp.data%2!=0:  #odd case
            if odd_head is None:
                odd_head = temp
                odd_tail = temp
            elif odd_tail is not None:
                odd_tail.next = temp
                odd_tail = odd_tail.next
        else:#even case
            if even_head is None:
                even_head=temp
                even_tail=temp
            elif even_tail is not None:
                even_tail.next = temp
                even_tail= even_tail.next
        temp = temp.next

    #all even case
    if odd_head is None:
        return even_head
    else:
        odd_tail.next=even_head

    if even_head is not None:
        even_tail.next =None
        
    return odd_head

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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
