# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# false 
# Sample Output 2 Explanation
# The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2. 


import queue
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class Graph:

    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
        
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.adjMatrix)
             
    def dfs(self,sv,visited):
        visited[sv] =True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]==1 and visited[i] is False:
                self.dfs(i,visited)
                visited[i]=True

    def isConnected(self):
        visited =[False for i in range(self.nVertices)]
        self.dfs(0,visited)

        for boolVal in visited:
            if not boolVal:
                return False
        return True

li = stdin.readline().strip().split()
V =int(li[0])
E =int(li[1])
if V ==0:
    print('true')
else:
    g = Graph(V)

    for i in range(E):
        arr = stdin.readline().strip().split()
        fv = int(arr[0])
        sv = int(arr[1])
        g.addEdge(fv,sv)
    print()
    if g.isConnected():
        print('true')
    else:
        print('false')
