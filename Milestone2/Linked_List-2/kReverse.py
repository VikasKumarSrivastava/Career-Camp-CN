# Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
#  'k' is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
# Example :
# Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

# For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

# For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4
#  Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 9 10 -1
# 4
# Sample Output 1 :
# 4 3 2 1 8 7 6 5 10 9
# Sample Input 2 :
# 2
# 1 2 3 4 5 -1
# 0
# 10 20 30 40 -1
# 4
# Sample Output 2 :
# 1 2 3 4 5 
# 40 30 20 10 

from sys import stdin
#TC = O(N)
#SC = O(N/K)
#LL is of N size
# n/k or (n/k)+1 calls will be made during the recursion
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def kReverse(head, k) :
	#Your code goes here
    if k == 0 or k ==1:
        return head
    current = head
    fwd = None
    prev = None
    count=0
    while (count< k ) and (current is not None):
        fwd = current.next
        current.next = prev
        prev = current
        current = fwd
        count+=1

    if fwd is not None:
        head.next= kReverse(fwd,k)
    return prev

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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
