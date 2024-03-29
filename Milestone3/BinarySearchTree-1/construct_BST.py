# Given a sorted integer array A of size n, which contains all unique elements. 
# You need to construct a balanced BST from this input array. Return the root of constructed BST.
# Note: If array size is even, take first mid as root.
# Sample Input 1:
# 7
# 1 2 3 4 5 6 7
# Sample Output 1:
# 4 2 1 3 6 5 7 

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBSTHelper(lst):
    if len(lst) == 0:
        return
    if len(lst)%2==0:
        mid = (len(lst))//2 - 1
    else:
        mid = (len(lst))//2
    root = BinaryTreeNode(lst[mid])
    root.left = constructBSTHelper(lst[:mid])
    root.right =  constructBSTHelper(lst[mid+1:])
    return root

def constructBST(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    return constructBSTHelper(lst)
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)
