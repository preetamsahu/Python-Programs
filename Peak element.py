#completed , all test cases pass
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if i==0:
        if arr[i]>arr[i+1]:
            print(i)
            break
    elif i<(len(arr)-1):
        if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            print(i)
            break
    else:
        if arr[i]>arr[i-1]:
            print(i)
            break