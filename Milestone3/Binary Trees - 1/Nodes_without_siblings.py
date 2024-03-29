# For a given Binary Tree of type integer, print all the nodes without any siblings.
# Sample Input 1:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output 1:
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

def printNodesWithoutSibling(root) :
	# Your code goes here
    if root == None:
        return
    if root.left is None and root.right is not None:
        print(root.right.data,end =' ')
    elif root.left is not None and root.right is None:
        print(root.left.data,end=' ')
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)
    
#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

	

# Main
root = takeInput()
printNodesWithoutSibling(root)
