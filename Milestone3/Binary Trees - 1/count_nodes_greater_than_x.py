# For a given a binary tree of integers and an integer X, find and return the total number of nodes of the given binary tree which are having data greater than X.
# The only line of output prints the total number of nodes where the node data is greater than X.
# Sample Input 1:
# 1 4 2 3 -1 -1 -1
# 2
# Sample Output 1:
# 2
# Explanation for Sample Input 1:
# Out of the four nodes of the given binary tree, [3, 4] are the node data that are greater than X = 2.
# Sample Input 2:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 5
# Sample Output 2:
# 3

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def countNodesGreaterThanX(root, x) :
	#Your code goes here
    if root == None:
        return 0
    if root.data > x:
        leftCount  = 1+ countNodesGreaterThanX(root.left,x)
        rightCount = countNodesGreaterThanX(root.right,x)
    else:
        leftCount  = countNodesGreaterThanX(root.left,x)
        rightCount = countNodesGreaterThanX(root.right,x)

    return leftCount+rightCount

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
x = int(stdin.readline().strip())

count = countNodesGreaterThanX(root, x)
print(count)
