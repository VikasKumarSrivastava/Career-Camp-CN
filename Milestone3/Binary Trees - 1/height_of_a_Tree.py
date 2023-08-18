# For a given Binary Tree of integers, find and return the height of the tree. 
# Height is defined as the total number of nodes along the longest path from the root to any of the leaf node.
# Sample Input 1:
# 10 20 30 40 50 -1 -1 -1 -1 -1 -1
# Sample Output 1:
# 3
# Sample Input 2:
# 3 -1 -1
# Sample Output 2:
# 1
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root) :
	#Your code goes here
    if root == None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return 1+max(leftHeight,rightHeight)

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

h = height(root)
print(h)
