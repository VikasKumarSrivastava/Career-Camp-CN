# For a given Binary Tree of integers, print the post-order traversal.
# Sample Input 1:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
#  Sample Output 1:
# 4 5 2 6 7 3 1 
# Sample Input 2:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
#  Sample Output 1:
# 2 9 3 6 10 5 

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def postOrder(root):
	#Your code goes here
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
postOrder(root)
