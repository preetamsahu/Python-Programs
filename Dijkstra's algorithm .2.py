'''
pred will conatin the path from src to that node
18
A B 2
A C 4
B A 2
B C 3
B D 8
C A 4
C B 3
C E 5
C D 2
D B 8
D C 2
D E 11
D F 22
E C 5
E D 11
E F 1
F D 22
F E 1

'''
import sys
from collections import defaultdict
import heapq
def dijsktra(graph,src='A',dest='F'):
    node_data=defaultdict()
    inf=sys.maxsize
    for i in graph:
        node_data[i]={'cost':inf,'pred':[]}
    node_data[src]['cost']=0
    temp=src

    for i in range(len(graph)):
        if
'''graph={
    'A':{'B':2,'C':4},
    'B':{'A':2,'C':3,'D':8},
    'C':{'A':4,'B':3,'E':5,'D':2},
    'D':{'B':8,'C':2,'E':11,'F':22},
    'E':{'C':5,'D':11,'F':1},
    'F':{'D':22,'E':1}
}
instead of initilizing it you can take input from user 
'''
e=int(input())
graph=defaultdict(dict)
for i in range(e):
    u,v,w=map(str,input().split())
    graph[u][v]=int(w)
dijsktra(graph)