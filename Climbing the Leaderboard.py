ranked=list(map(int,input().split()))
player=list(map(int,input().split()))
cnt=1
rank=[1]
for i in range(1,len(ranked)):
    if ranked[i-1]==ranked[i]:
        rank.append(cnt)
    else:
        cnt+=1
        rank.append(cnt)
ans=[]
for i in player:
    k=0
    for j in range(len(ranked)):
        if i==ranked[j]:
            ans.append(rank[j])
            k=1
        elif i>ranked[j]:
            k=1
            ans.append(rank[j]-1)
            break
    if k==0:
        ans.append(rank[-1]+1)
print(ans)