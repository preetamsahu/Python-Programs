def merge(arr,l,h,mid):
    left=arr[l:mid+1]
    right=arr[mid+1:h+1]
    print(left,right)
    i=0
    j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    if i!=(len(left)-1):
        for i in range(i,len(left)):
            arr[k]=left[i]
            k+=1
    elif j!=(len(right)-1):
        for j in range(j,len(right)):
            arr[k]=right[j]
            k+=1
    return arr
array=list(map(int,input().split()))
l,h,mid=map(int,input().split())
print(merge(array,l,h,mid))
'''
1 3 5 7 8 9 10 -1 2 4 6
0 10 6  
'''