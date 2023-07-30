# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.
# Sample Input 1 :
# 1 
# 3 4 5 2 6 1 9 -1
# 3
# Sample Output 1 :
# 3 4 5 6 1 9
from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head) :
    #Your code goes here
    if head is None:
        return 0
    curr = head
    size= 0
    while curr.next is not None:
        size+=1
        curr=curr.next
    return size +1
def deleteNode(head, pos) :
    # Write your code here.
    if head is None:
        return
    size = length(head)    
    if pos > size:
        return head
    else:
        curr = head
        prev = head
        count = 0
        i=0
        while curr is not None:
            if pos == 0:
                head = head.next
                break
            if count  == pos-1:
                prev.next = curr.next
                break
            else:
                count = count +1
            if i ==0:
                curr = curr.next
                i=i+1
            curr = curr.next
            prev = prev.next
        return head

# Taking Input Using Fast I/O.
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



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
