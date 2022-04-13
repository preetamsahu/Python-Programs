s=input()
ans=[]
def is_pali(st):
    p=0
    for i in st:
        if i==i[::-1]:
            p+=1
    if p==len(st):
        return 1
    else:
        return 0
ans.append(list(s))
de
print(ans)