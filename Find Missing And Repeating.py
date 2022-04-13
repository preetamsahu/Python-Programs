N=int(input())
arr=list(map(int,input().split()))
cnt=[0 for i in range(N+1)]
ans=[]
for i in arr:
    cnt[i]+=1
for i in range(1,len(cnt)):
    if cnt[i]==2:
        ans.append((i))
for i in range(1,len(cnt)):
    if cnt[i]==0:
        ans.append(i)

print(ans)

