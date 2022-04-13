'''reflowers flow flight'''
strs=list(map(str,input().split()))
length=[]
for i in strs:
    length.append(len(i))
min_str=strs[length.index(min(length))]

l=0
ans=''
for i in range(1,len(min_str)+1):
    cnt = 0
    for j in strs:
        if min_str[:i] in j[:i]:
            cnt+=1
    if cnt==len(strs):
        if l<len(min_str[:i]):
            l=len(min_str[:i])
            ans=min_str[:i]
print(ans)
