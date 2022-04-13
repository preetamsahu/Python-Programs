INF=float('inf')
def printmat(mat):
    r,c=len(mat),len(mat[0])
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end="\t")
        print()
def floyedwarshall(mat,vrtx):
    for k in range(vrtx):
        for i in range(vrtx):
            for j in range(vrtx):
                if (mat[i][k]+mat[k][j])<mat[i][j]:
                    mat[i][j]=mat[i][k]+mat[k][j]
    printmat(mat)
V,E=map(int,input().split())
matrix=[[0]*V for i in range(V)]
#first we initialise to 0 if i==j and those where src!=dest initialise to max value (infinite)
for i in range(V):
    for j in range(V):
        if i==j:
            matrix[i][j]=0
        else:
            matrix[i][j]=INF

#then we will take input
for _ in range(E):
    u,v,w=map(int,input().split())
    matrix[u][v]=int(w)

printmat(matrix)
floyedwarshall(matrix,V)
# printmat(allshortestpat)
'''
4 4
0 3 10
0 1 5
1 2 3
2 3 1
'''