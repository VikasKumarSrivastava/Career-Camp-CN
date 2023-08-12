# Given a Singly Linked List of integers, delete all the alternate nodes in the list.
# Example:
# List: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> null
# Alternate nodes will be:  20, 40, and 60.
# Hence after deleting, the list will be:
# Output: 10 -> 30 -> 50 -> null
# Sample Input 1:
# 1 2 3 4 5 -1
# Sample Output 1:
# 1 3 5
# Explanation of Sample Input 1:
# 2, 4 are alternate nodes so we need to delete them 
# Sample Input 2:
# 10 20 30 40 50 60 70 -1
# Sample Output 2:
# 10 30 50 70 
''' 
    Following is the node structure

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def deleteAlternateNodes(head):
    # Write your code here
    if head is None:
        return None

    curr = head
    currNext  = head

    while curr != None and curr.next !=None:
        currNext = curr.next
        curr.next = curr.next.next

        curr = curr.next
