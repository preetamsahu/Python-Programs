'''
for topological sort the graph should be directed acyclic and if there is an edge from u to v the u comes before
v
test case
5 7
A C
A D
B A
B D
C E
D C
D E
'''
from sys import maxsize
from collections import defaultdict
def getnumber():
    return 0
def getdegree(graph):
    degree=defaultdict(getnumber)
    for i in graph:
        degree[i]=0
    for i in graph:
        for adjcy in graph[i]:
            degree[adjcy]+=1
    return degree
def getmin(dictt):
    min_value=0
    node=''
    for i in dictt:
        if dictt[i]<=min_value:
            min_value=dictt[i]
            node=i
    return node

def topological(graph,vertex):
    graphX=graph
    for i in range(vertex):
        indegree = getdegree(graphX)
        min_degree=getmin(indegree)
        print(min_degree)
        graphX.pop(min_degree)

graph=defaultdict(list)
V,E=map(int,input().split())
for i in range(E):
    u,v=map(str,input().split())
    graph[u].append(v)
for i in graph:
    print(i,graph[i])
indeg=getdegree(graph)
print(indeg)
topological(graph,V)