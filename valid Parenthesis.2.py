S=input()
left=0
right=0
for i in range(len(S)):
    if S[i]=='(':
        left+=1
    elif S[i]==')' and left>right:
        right+=1
    else:
        ans=min(left,right)
        right=0
        left=0

ans=min(left,right)
print(ans*2)