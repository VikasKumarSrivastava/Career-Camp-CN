# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5
# TC O(E *log(V))
# SC O(V^2)
import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt

    def removeEdge(self):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __getMinVertexD(self,visited,weight):       
        min_vertex=-1
        for i in range(self.nVertices):
            if(visited[i] is False and (min_vertex==-1 or weight[min_vertex]>weight[i])):
                min_vertex=i
        return min_vertex
        
    def djikstra(self):
        visited = [False for i in range(self.nVertices)]
        dist=[sys.maxsize for i in range(self.nVertices)]
        dist[0] = 0
        for i in range(self.nVertices-1):
            minVertex = self.__getMinVertexD(visited,dist)
            visited[minVertex] = True

            for j in range(self.nVertices):
                if self.adjMatrix[minVertex][j]> 0 and visited[j] is False:
                    if dist[j]>dist[minVertex]+ self.adjMatrix[minVertex][j]:
                        dist[j]=dist[minVertex]+self.adjMatrix[minVertex][j]
        for i in range(self.nVertices):
            print(str(i)+" "+str(dist[i]))

li=[int(ele) for ele in input().split()]
n=li[0]
E=li[1]

g=Graph(n)
for i in range(E):
    curr_input=[int(ele) for ele in input().split()]
    g.addEdge(curr_input[0],curr_input[1],curr_input[2])
g.djikstra()
