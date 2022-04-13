#Time limit exceed
arr=list(map(int,input().split()))
ans=[-1]
sets=[]
key=0
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        ans.append(arr[i-1])
        sets.append(arr[i-1])
    else:
        key=0
        for j in range(len(sets)-1,0,-1):
            if sets[j]<arr[i]:
                k=1
                ans.append(sets[j])
        if key==0:
            ans.append(-1)
print(ans)