arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

def merge(arr1,arr2):
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            print(arr1[i],end=" ")
            i+=1
        else:
            print(arr2[j],end=" ")
            j+=1
    if i!=(len(arr1)-1):
        for i in range(i,len(arr1)):
            print(arr1[i],end=" ")
    elif j!=(len(arr2)-2):
        for j in range(j,len(arr1)):
            print(arr2[j],end=" ")
merge(arr1,arr2)
