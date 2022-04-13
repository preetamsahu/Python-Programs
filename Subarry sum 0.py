arr=list(map(int,input().split()))

summ=0
for i in range(0,len(arr)+1):
    for j in range(i+1,len(arr)+1):
        list1.append(arr[i:j])
p=0
for i in list1:
    if sum(i)==0:
        p=1
        print("true")
if p==0:
    print("false")