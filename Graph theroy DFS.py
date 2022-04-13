"""BFS stands for breadth first search """
from collections import defaultdict
graph=defaultdict(list)
V,E=map(int,input().split())
for i in range(E):
    v,u=map(str,input().split())
    graph[v].append(u)
    graph[u].append(v)
for v in graph:
    print(v,graph[v])

#BFS implementation by me
def BFS(graph,start):
    queue=[]
    queue.append(start)
    path=[]
    visited=defaultdict(bool)
    visited[start]=True
    while len(queue)>0:
        st = queue[0]
        for vertices in graph[st]:
            if vertices not in queue and visited[vertices]==False:
                queue.append(vertices)
        path.append(st)
        visited[st]=True
        queue.remove(st)
    return path
""" DFS means pre, in , post order traversla"""
def DFS(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for vertex in graph[start]:
        if visited[vertex]==False:
            DFS(graph,vertex,visited,path)
    return path

path=[]
visited=defaultdict(bool)#default value will be false
start='A'
print("DFS travers",DFS(graph,start,visited,path))
print("BFS traverse",BFS(graph,'A'))
