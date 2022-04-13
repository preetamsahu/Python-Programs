N=int(input())
arr=list(map(int,input().split()))
K=int(input())
#TODO: Insertion sort tecnique but it is slower that python in built sorted function
for i in range(1,len(arr)):
    key=arr[i]
    j=i
    while j>0 and arr[j-1]>key:
        arr[j]=arr[j-1]
        j-=1
    arr[j]=key
print(arr)
print(arr[K-1])