arr=list(map(int,input().split()))
maximum=max(arr)
lst=list()
if maximum>=0:
    lst=[0 for i in range(maximum+2)]
for i in arr:
    if i>0:
        lst[i]=1
for i in range(1,len(lst)):
    if lst[i]==0:
        print(i)
        break