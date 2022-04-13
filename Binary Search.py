
import bisect
#TODO bisect is inbuilt binary search in python bisect.bisect_left(array,key,lo=0,high=len(array)) last tow parameters are optional they are used to search in sub array
#TODO bisext.bisect_left() return the first left most occurance of key
def binary_Search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
key=int(input())
arr=list(map(int,input().split()))
ind=binary_Search(arr,key)
if ind==-1:
    print("Not found")
else:
    print(f"Index of {key} in array is {ind+1}")
########################################################################################################
print(bisect.bisect_left(arr,key))

'''
9
1 2 3 4 5 6 7 8 9
'''