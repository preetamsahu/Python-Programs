#single source shortest path : greedy approach
#we will use heap data structure
'''test case
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D----> this one is sourse and destination respectively
'''
import heapq #heapq is inbuilt queue
from collections import defaultdict

def dijkstra(graph,src,dest):
    h=[]
    '''
    keep a track record of verties with the cost 
    heappop will return vertex with least cost 
    g
    '''

graph=defaultdict(list)
v,e=map(int,input().split())
for _ in range(e):
    u,v,w=map(str,input().split())
    graph[u].append((v,int(w)))
for i in graph:
    print(i,graph[i])

src,dest=map(str,input().split())
di