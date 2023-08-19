# For a given a Binary Tree of type integer, print the complete information of every node, when traversed in a level-order fashion.
# To print the information of a node with data D, you need to follow the exact format :

#            D:L:X,R:Y

# Where D is the data of a node present in the binary tree. 
# X and Y are the values of the left(L) and right(R) child of the node.
# Print -1 if the child doesn't exist.
# Sample Input 1:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
#  Sample Output 1:
# 8:L:3,R:10
# 3:L:1,R:6
# 10:L:-1,R:14
# 1:L:-1,R:-1
# 6:L:4,R:7
# 14:L:13,R:-1
# 4:L:-1,R:-1
# 7:L:-1,R:-1
# 13:L:-1,R:-1
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
#  Sample Output 2:
# 1:L:2,R:3
# 2:L:4,R:5
# 3:L:6,R:7
# 4:L:-1,R:-1
# 5:L:-1,R:-1
# 6:L:-1,R:-1
# 7:L:-1,R:-1

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    # Your code goes here
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)

    while not pendingNodes.empty():
        stringToPrint =""
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)
        
        else:
            print(str(str(frontNode.data)+":L:"),end="")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)
                print(str(str(frontNode.left.data)+",R:"),end="")

            else:
                print(str("-1,R:"),end="")
            
            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)
                print(str(frontNode.right.data))

            else:
                print(-1)

        
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
printLevelWise(root)
