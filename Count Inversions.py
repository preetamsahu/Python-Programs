#need optimization
N=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i]>arr[j]:
            cnt+=1
print(cnt)
