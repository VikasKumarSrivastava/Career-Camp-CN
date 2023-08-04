# You have been given a singly linked list of integers along with two integers, 'i,' and 'j.' Swap the nodes that are present at the 'i-th' and 'j-th' positions.
# Note :
# Remember, the nodes themselves must be swapped and not the datas.
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 3 4
# Sample Output 1 :
# 3 4 5 6 2 1 9 
#  Sample Input 2 :
# 2
# 10 20 30 40 -1
# 1 2
# 70 80 90 25 65 85 90 -1
# 0 6
#  Sample Output 2 :
# 10 30 20 40 
# 90 80 90 25 65 85 70 

from sys import stdin
#TC O(N)
#SC O(1)
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def swapNodes(head, i, j) :
	#Your code goes here
    if i == j :
        return head
    currentNode = head
    prev =None
    firstNode = None
    secondNode=None
    firstNodePrev =None
    secondNodePrev=None

    pos = 0
    while currentNode is not None:
        if pos == i:
            firstNodePrev=prev
            firstNode = currentNode
        elif pos ==j:
            secondNodePrev=prev
            secondNode = currentNode
        prev = currentNode
        currentNode =currentNode.next
        pos+=1

    if firstNodePrev is not None:
        firstNodePrev.next = secondNode
    else:
        head = secondNode

    if secondNodePrev is not None:
        secondNodePrev.next = firstNode
    else:
        head = firstNode
    
    currentfirstNode  = secondNode.next
    secondNode.next = firstNode.next
    firstNode.next =currentfirstNode

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

def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
