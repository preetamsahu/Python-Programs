arr=list(map(int,input().split()))
if len(arr)==0:
    print(0)
else:
    hight=1
    cnt=0
    for i in range(1,len(arr)):
        cnt+=1
        if cnt==2**(hight+1):
            hight+=1
            cnt=0
