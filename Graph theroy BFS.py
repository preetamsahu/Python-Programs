"""Queue is used """
""" In this we will use double ended queue i.e. deque defind in collections module"""
from collections import deque
from collections import defaultdict

#first we take graph as input in this we are using undirected graph
V,E=map(int,input().split())
graph=defaultdict(list)
for _ in range(E):
    v,u=map(str,input().split())
    graph[v].append(u)
    graph[u].append(v)
for vertex in graph:
    print(vertex,graph[vertex])

def BFS(graph,start):
    path=[]
    queue=deque()
    queue.append(start)
    path.append(start)
    visited=defaultdict(bool)
    visited[start]=True
    while len(queue)!=0:
        st=queue.popleft()
        for vertex in graph[st]:
            if visited[vertex]==False:
                queue.append(vertex)
                path.append(vertex)
                visited[vertex]=True
    return path

print(BFS(graph,'A'))