# Given a BST and an integer k. 
# Find if the integer k is present in given BST or not. You have to return true, if node with data k is present, return false otherwise.
# Sample Input 1 :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 2
# Sample Output 1 :
# true
# Sample Input 2 :
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# 12
# Sample Output 2 :
# false
  
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Solution
def searchInBST(root, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return False
    # print(root.data)
    if root.data == k:
        return True
    if root.data<k:
        return searchInBST(root.right,k)
    elif root.data>k:
        return searchInBST(root.left,k)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
ans = searchInBST(root, k)
# print('ans is ',ans)
if ans:
    print("true")
else:
    print("false")
