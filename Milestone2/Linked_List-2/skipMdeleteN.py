# You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' 
# Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.
# To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# 2 2
# Sample Output 1 :
# 1 2 5 6
# Sample Input 2 :
# 2
# 10 20 30 40 50 60 -1
# 0 1
# 1 2 3 4 5 6 7 8 -1
# 2 3
# Sample Output 2 :
# 1 2 6 7
# Explanation of Sample Input 2 :
# For the first query, we delete one node after every zero elements hence removing all the items of the list. Therefore, nothing got printed.

# For the second query, we delete three nodes after every two nodes, resulting in the final list, 1 -> 2 -> 6 -> 7.
from sys import stdin
#TC =O(N)
#SC=O(1)
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N) :
	#Your code goes here
    if M==0 or head is None:
        return None
    if N==0:
        return head
    current_node = head
    temp =None
    while current_node is not None:
        take=0
        skip = 0
        while current_node is not None and take<M:
            if temp is None:
                temp = current_node
            else:
                temp.next = current_node
                temp= current_node
            current_node=current_node.next
            take+=1

        while current_node is not None and skip<N:
            current_node=current_node.next
            skip+=1
    
    if temp is not None:
        temp.next = None
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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
