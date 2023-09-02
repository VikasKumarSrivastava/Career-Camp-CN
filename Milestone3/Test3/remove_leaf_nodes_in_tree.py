# Remove all leaf nodes from a given generic Tree. Leaf nodes are those nodes, which don't have any children.
# Note : Root will also be a leaf node if it doesn't have any child. You don't need to print the tree, just remove all leaf nodes and return the updated root.
# Input format :
# Line 1 : Elements in level order form separated by space (as per done in class). Order is - `

# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element `
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1 : (Level wise, each level in new line)
# 10
# 20
## Read input as specified in the question.
## Print output as specified in the question.
import queue 
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def removeLeafNodes(root):
    #Implement Your Code Here
    if len(root.children) ==0:
        return None
    node_remove=[]
    for child in root.children:
        ans = removeLeafNodes(child)
        if ans is None:
            node_remove.append(child)
    for node in node_remove:
        root.children.remove(node)
    return root

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def printLevelWiseTree(root):
    q = queue.Queue()
    q.put(root)
    q.put(None)
    
    while q.empty() is False:
        front = q.get()
        if front is None:
            if q.empty():
                return
            else:
                print()
                q.put(None)
        else:
            print(front.data,end= ' ')
            for child in front.children:
                q.put(child) 
# Main
arr = list(int(x) for x in input().strip().split(' '))
root = createLevelWiseTree(arr)
removeLeafNodes(root)
printLevelWiseTree(root)
