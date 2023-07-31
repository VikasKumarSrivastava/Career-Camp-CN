class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    smallHead=insertAtIR(head.next,i-1,data)
    head.next=smallHead
    return head
