from math import ceil
arr=list(map(int,input().split()))
element=int(input())
def binary_search(array,l,r):
    mid=ceil((l+r)//2)
    if l>r:
        print("Not found")
        return
    elif array[mid]==element:
        print(f"Your element found {mid+1}")
        return
    else:
        if array[mid]>element:
            r=mid-1
            binary_search(array,l,r)
        else:
            l=mid+1
            binary_search(array,l,r)
binary_search(arr,0,len(arr)-1)
