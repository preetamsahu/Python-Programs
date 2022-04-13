arr=list(map(int,input().split()))
arr2=sorted(arr)
ans=[]
for i in range(len(arr)):
    if arr2.index(arr[i])==len(arr)-1:
        ans.append(-10000000)
    else:
        k=arr2.index(arr[i])
        while k<len(arr)-1:
            if arr2[k+1]==arr2[k] and k<len(arr):
                k+=1
            else:
                break
        if k==len(arr)-1:
            ans.append(-10000000)
        else:
            ans.append(arr2[k])
print(ans)