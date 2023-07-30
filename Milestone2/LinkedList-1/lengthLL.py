# Given the head of a singly linked list of integers, find and return its length.
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
