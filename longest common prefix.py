''' flowers flow flight '''
def subString(s):
    n=len(s)
    substr=[]
    for i in range(1,len(s)):
        substr.append(s[:i])
    return substr

strs=list(map(str,input().split()))
substrs=list()
for string in strs:
    substrs.append(subString(string))
lenght=[]

for i in substrs:
    lenght.append(len(i))
min_len=min(lenght)
ind=lenght.index(min_len)
l=0
ans=''
for st in substrs[ind]:
    cnt=0
    for i in substrs:
        if st in i:
            cnt+=1
    if cnt==len(substrs):
        if len(st)>l:
            l=len(st)
            ans=st
print(ans)
