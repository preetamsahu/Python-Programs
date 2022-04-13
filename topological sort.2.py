#we will store graph in adjacency list
from collections import defaultdict
V,E=map(int,input().split())
graph=defaultdict(list)

def topologicalSort(graph,vrtx):
    indegree=[0]*vrtx
    for node in graph:
        for adj in graph[node]:
            indegree[adj]+=1
    bfs=[i for i in range(vrtx) if indegree[i]==0]
    for node in bfs:
        for adj in graph[node]:
            indegree[adj]-=1
            if indegree[adj]==0:
                bfs.append(adj)
    return bfs

for i in range(E):
    v,u=map(str,input().split())
    v=-ord('A')+ord(v)
    u=-ord('A')+ord(u)
    graph[v].append(u)
for i in graph:
    print(i,graph[i])
toplogy=topologicalSort(graph,V)
if len(toplogy)==0:
    print("NO topology found")
else:
    for i in toplogy:
        print(chr(ord('A')+i),end=' ')
'''
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