# Following is the Node class already written for the Linked List
# You have been given a singly linked list of integers.
# Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.
# Sample Input 1 :
# 2
# 3 4 5 2 6 1 9 -1
# 5
# 10 20 30 40 50 60 70 -1
# 6
# Sample Output 1 :
# 2
# -1
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    if head is None:
        return -1
    if head.data == n:
        return 0
    smallOutput = findNode(head.next,n)
    if smallOutput ==-1:
        return -1
    else:
        return smallOutput + 1
