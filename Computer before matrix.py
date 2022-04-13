N,M=map(int,input().split())
arr=[]
for i in range(N):
    lst=list(map(int,input().split()))
    arr.append(lst)
def till_Sum(x,y,arr):
    summ=0
    for i in range(x):
        for j in range(y):
            summ+=arr[i][j]
    return summ
ans=[[0]*M for i in range(N)]
ans[0][0]=arr[0][0]
for i in range(N):
    lst=[]
    for j in range(1,N):
        print()
        k=arr[i][j]-till_Sum(i,j,ans)
print(ans)
'''
1 3
1 3 5
ans={{1, 2, 2}}
'''