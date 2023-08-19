# For a given Binary Tree of type integer and a number K, 
# print out all root-to-leaf paths where the sum of all the node data along the path is equal to K.
# Sample Input 1:
# 2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1
# 13
#  Sample Output 1:
# 2 3 4 4 
# 2 3 8
# Sample Input 2:
# 5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
# 13
#  Sample Output 2:
# 5 6 2
# 5 7 1

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToKHelper(root,k,path,currSum):
    if root is None:
        return
    if root.left is None and root.right is None:
        currSum+=root.data

        if currSum == k:
            print(str(path+str(root.data)+" ").lstrip())
        return
    rootToLeafPathsSumToKHelper(root.left,k,str(path+str(root.data)+" "),(currSum +root.data))
    rootToLeafPathsSumToKHelper(root.right,k,str(path+str(root.data)+" "),(currSum +root.data))
    

def rootToLeafPathsSumToK(root, k):
	#Your code goes here
    rootToLeafPathsSumToKHelper(root,k,"",0)


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

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k)
