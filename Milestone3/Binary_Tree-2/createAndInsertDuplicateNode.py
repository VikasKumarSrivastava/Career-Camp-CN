# For a given a Binary Tree of type integer, duplicate every node of the tree and attach it to the left of itself.
# The root will remain the same. So you just need to insert nodes in the given Binary Tree.

# Sample Input 1:
# 10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1
# Sample Output 1:
# 10 
# 10 30 
# 20 30 60 
# 20 50 60 
# 40 50 
# 40 
# Sample Input 2:
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# Sample Output 2:
# 8 
# 8 10 
# 5 10 
# 5 6 
# 2 6 7 
# 2 7


from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# TC =O(N)
# SC =O(H)
# H is equal to log(N) for a Balanced tree
#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertDuplicateNode(root):
    # Your code goes here
    if root is None:
        return
    newNode = BinaryTreeNode(root.data)
    rootLeft = root.left

    root.left = newNode
    newNode.left  = rootLeft

    insertDuplicateNode(rootLeft)
    insertDuplicateNode(root.right)


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

insertDuplicateNode(root)
printLevelWise(root)
