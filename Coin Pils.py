k=int(input())
arr=list(map(int,input().split()))
arr.sort()
i=0
cnt1=0
j=len(arr)-1
while i<j:
    if abs(arr[i]-arr[j])>=k:
        cnt1+=1
        j-=1
    elif abs(arr[i]-arr[j])<k:
        i+=1
        j-=1
ans=[]
ans.append(cnt1)
cnt2=0
i=0
j=len(arr)-1
while i<j:
    if abs(arr[i]-arr[j])>=k:
        cnt2+=1
        i+=1
    else:
        i+=1
        j-=1
ans.append(cnt2)
print(ans,arr)
'''
4
7 1 1 10 9 8 6 2 3 3
10
'''