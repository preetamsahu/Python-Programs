#not satisfying all the cases
#012
s=input()
i=0
if s[0]=='.':
    print(0)
elif s.count('.')!=3:
    print(0)

while i<len(s):
    k=''
    while i<len(s) and s[i]!='.':
        k=k+s[i]
        i+=1
    i+=1
    try:
        k=int(k)
    except:
        print(k)
        print(0)
        break
    if 0<=int(k)<=255:
        pass
    else:
        print(k)
        print(0)
        break
print("valid")