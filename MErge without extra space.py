arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
x=len(arr1)-1
y=len(arr2)-1
for i in range(y,-1,-1):
    if arr2[i]>=arr1[x]:
        pass
    else:
        arr2[i],arr1[x]=arr1[x],arr2[i]
        k = x
        print(k,arr1,arr2)
        # while k>0:
        #     if arr1[k-1]>arr1[k]:
        #         arr1[k-1],arr1[k]=arr1[k],arr1[k-1]
        #         k=k-1
        #     else:
        #         break
        arr1.sort()

print(arr1)
print(arr2)