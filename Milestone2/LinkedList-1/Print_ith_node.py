# For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.
# Assume that the Indexing for the singly linked list always starts from 0.
# If the given position 'i',  is greater than the length of the given singly linked list, then don't print anything.
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3
# Sample Output 1 :
# 2


from sys import stdin

#Following is the Node class already written for the Linked List
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


def printIthNode(head, i):
    #Your code goes here
    if head is None:
        return
    size = length(head)    
    if i > size:
        return
    else:
        curr = head
        count = 0
        while curr is not None:
            if count  == i:
                print(curr.data)
                break
            else:
                count = count + 1
            curr = curr.next

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
    i = int(stdin.readline().rstrip())
    printIthNode(head, i)

    t -= 1
