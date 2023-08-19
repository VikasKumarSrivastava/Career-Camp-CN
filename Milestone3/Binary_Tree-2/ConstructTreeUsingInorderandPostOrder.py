# For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists.
# You just need to construct the tree and return the root.
# Sample Input 1:
# 7
# 4 5 2 6 7 3 1 
# 4 2 5 1 6 3 7 
# Sample Output 1:
# 1 
# 2 3 
# 4 5 6 7 
# Sample Input 2:
# 6
# 2 9 3 6 10 5 
# 2 6 3 9 5 10 
# Sample Output 2:
# 5 
# 6 10 
# 2 3 
# 9 
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreeHelper(postOrder,inOrder):
    if len(postOrder)==0:
        return None
    rootData=postOrder[-1]
    root=BinaryTreeNode(rootData)
    rootIndexInInOrder=-1
    for i in range(0,len(inOrder)):
        if inOrder[i]==rootData:
            rootIndexInInorder=i
            break
    if rootIndexInInorder==-1:
        return None
        
    leftInorder=inOrder[0:rootIndexInInorder]
    rightInorder=inOrder[rootIndexInInorder+1:]
        
    lenLeftSubtree=len(leftInorder)
        
    leftpostOrder=postOrder[0:lenLeftSubtree]
    rightpostOrder=postOrder[lenLeftSubtree:-1]
        
    leftChild=buildTreeHelper(leftpostOrder,leftInorder)
    rightChild=buildTreeHelper(rightpostOrder,rightInorder)
        
    root.left=leftChild
    root.right=rightChild
    return root

def buildTree(postOrder, inOrder, n) :
	#Your code goes here
    return buildTreeHelper(postOrder,inOrder)


'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)
