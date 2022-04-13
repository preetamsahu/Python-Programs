#Tree is graph which doesn't have a cycle and have n-1 edge where n is the numbberr of nodes
#weighted graph is graph in which every edge a have some weight
#we can represent the graph by adjancency matrix or adjancecy list both have different

"""Adjancecy list for undirected graph"""
#V=7 and E=9
"""
A B
A C
A F
C E
C F
C D
D G
D E
G F
"""
#Here defaultdict is dictionary that does not arise a key value error that means if
#key is not defind then it insert that key and the value of that key is depends on the
#parameter which you passes in defaultdict
""" for example defaultdict(list) in this if I access a key which i have not defind the
the value of that key will be list type data structure"""
from collections import defaultdict
V,E=map(int,input().split())
graph=defaultdict(list)
for i in range(E):
    v,u=map(str,input().split())
    graph[v].append(u)
    graph[u].append(v)
for v in graph:
    print(v,graph[v])