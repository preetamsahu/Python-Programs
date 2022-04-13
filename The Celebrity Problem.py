N=int(input())
mat=list()
for i in range(N):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(N):
    if sum(mat[i])==0:
        x=0
        for j in range(N):
            if i!=j and mat[j][i]==1:
                x+=1
        if x==(N-1):
            print(i)
            break
print(-1)