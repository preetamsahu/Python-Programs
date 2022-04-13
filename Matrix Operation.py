'''
2 2
0
1
1
0

'''
''''''
n,m=map(int,input().split())
matrix=[]
for i in range(n):
    lst=[int(x) for x in input().strip().split()]
    matrix.append(lst)
direction='r'
i=0
j=0
while i<=n and j<=m:
    if i>=n or j>=m or i<0 or j<0:
        if i>=n and j>=m:
            i-=1
            j-=1
        elif i>=n:
            i-=1
        elif j>=m:
            j-=1
        elif i<0 and j<0:
            i+=1
            j+=1
        elif i<0:
            i+=1
        else:
            j+=1
        tup=(i,j)
        print(tup)
        break
    if matrix[i][j]==0:
        print(matrix[i][j])
        if direction=='r':
            j+=1
        elif direction=='d':
            i+=1
        elif direction=='l':
            j-=1
        else:
            i-=1
    else:
        matrix[i][j]=0
        if direction=='r':
            direction = 'd'
            i+=1
        elif direction=='d':
            direction = 'l'
            j-=1
        elif direction=='l':
            direction = 'u'
            i-=1
        else:
            direction = 'r'
            j+=1
'''
3 5
0
1
1
1
0
1
0
1
0
1
1
1
1
0
0
'''

