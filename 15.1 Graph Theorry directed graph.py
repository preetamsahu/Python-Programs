"""we will implement undirected unweighted graph using adjacency matric"""
"""
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
"""
def printmatrx(matrx):
    for i in range(len(matrx)):
        for j in range(len(matrx)):
            print(matrx[i][j],end='\t')
        print()
v,e=map(int,input().split())
matrix=[[0]*v for i in range(v)]
'''
#for unweighted graph
for i in range(e):
    u,v,=map(str,input().split())
    u=ord(u)-ord('A')
    v=ord(v)-ord('A')
    matrix[u][v]=1
    matrix[v][u]=1

printmatrx(matrix)
'''
#for weighted and directed graph
'''
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
'''
for i in range(e):
    u,v,w=map(str,input().split())
    u=ord(u)-ord('A')
    v=ord(v)-ord('A')
    matrix[u][v]=int(w)
printmatrx(matrix)