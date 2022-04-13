s,x=map(str,input().split())
i=0
j=len(x)
while j<len(s):
    if x==s[i:j]:
        print(i)
    i+=1
    j+=1
print(-1)