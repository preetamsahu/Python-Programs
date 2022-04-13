lst = list(map(int,input().split()))
i=0
j=len(lst)-1
while i<j:
    lst[i],lst[j]=lst[j],lst[i]
    i+=1
    j-=1
print(lst)