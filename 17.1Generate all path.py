""" in this we assume that first element will be starting node and the last node
that seat in bottom rigght will be the destination"""
'''left (sourse)  bottom right(destnation)'''
#dfs/ recursively
''' index-> matrix[i][j]
first check if the prsent index is valid
check if the current index can be explored 
move right , down , diaonal
else backtrack
3
1 2 3
4 5 6
7 8 9

we will find all path from 1 to 9
'''
def findPath(path,i,j):
    r,c=len(mat),len(mat[0])
    #if destination is reached
    #print the path
    if i==r-1 and j==c-1:
        print(path+[mat[i][j]])#I can't understand why path.append is not working here
        return

    #explore
    if 0<=i<=(r-1) and 0<=j<=(c-1):
        path.append(mat[i][j])
    #mov right
    if 0<=i<=(r-1) and 0<=(j+1)<=(c-1):
        findPath(path,i,j+1)
    #mov down
    if 0<=(i+1)<=(r-1) and 0<=(j)<=(c-1):
        findPath(path,i+1,j)
    #mov diagonal
    if 0<=(i+1)<=(r-1) and 0<=(j+1)<=(c-1):
        findPath(path,i+1,j+1)
    # backtrack

    if len(path)>0:
        path.pop()
n=int(input())# numberr of row
mat=[]
path=[]
for i in range(n):
    elements=list(map(int,input().split()))
    mat.append(elements)
findPath(path,0,0)