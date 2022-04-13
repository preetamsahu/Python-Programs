arr=list(map(int,input().split()))
left=[arr[0]]
for i in range(1,len(arr)):
    if left[i-1]<arr[i]:
        left.append(arr[i])
    else:
        left.append(left[i-1])
right=[0 for i in range(len(arr))]
right[len(arr)-1]=arr[len(arr)-1]
for i in range(len(arr)-2,-1,-1):
    if right[i+1]<arr[i]:
        right[i]=arr[i]
    else:
        right[i]=right[i+1]
water=0
for i in range(len(arr)):
    water=water+min(left[i],right[i])-arr[i]
print(water)