arr=list(map(int,input().split()))
# i=0
# j=len(arr)-1
# while i<j:
#     if arr[i]==0:
#         i+=1
#     if arr[j]==2:
#         j-=1
#     else:
#         if arr[i]==2 and arr[j]==0:
#             arr[i],arr[j]=arr[j],arr[i]
#
i=0
mid=0
j=len(arr)-1
while mid<j:
    # print("hey")
    if arr[mid]==0:
        arr[mid],arr[i]=arr[i],arr[mid]
        mid+=1
        i+=1
    elif arr[j]==0:
        arr[j],arr[i]=arr[i],arr[j]
        j-=1
        i+=1
    elif arr[mid]==2:
        arr[mid],arr[j]=arr[j],arr[mid]
        mid+=1
        j-=1
    elif arr[mid]==1:
        mid+=1
    elif arr[j]==2:
        j-=1
print(arr)

