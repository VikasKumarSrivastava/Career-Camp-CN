# For a given a Binary Tree of integers, replace each of its data with the depth of the tree.
# Root is at depth 0, hence the root data is updated with 0. Replicate the same further going down the in the depth of the given tree.
# The modified tree will be printed in the in-order fashion.
#  Sample Input 1:
# 2 35 10 2 3 5 2 -1 -1 -1 -1 -1 -1 -1 -1 
# Sample Output 1:
# 2 1 2 0 2 1 2 
#  Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 2 1 2 0 2 1 2 
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def solve(root,depth=0):
    if root == None:
        return
    root.data = depth
    solve(root.left,depth+1)
    solve(root.right,depth+1)

def changeToDepthTree(root) :
	#Your code goes here
    return solve(root)

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


def inOrder(root) :
	if root is None :
		return 

	inOrder(root.left)
	print(root.data, end = " ")
	inOrder(root.right)
	

# Main
root = takeInput()

changeToDepthTree(root)
inOrder(root)
