'''
Given a rotated sorted list that was rotated a unknown number of times you need to find the
number of times the sorted list wast rotated
here rotating means removing the last element and adding it before the first element ib the list

first logic that comes in mind is that if a sorted list is rotated 'k' times then the smallest element
will be in kth position
'''
def count_rotation_linear(arr1):
    for i in range(len(arr1) - 1):
        if arr1[i] < arr1[i + 1]:
            pass
        else:
            return i+1
    return 0

def count_rotation_logrithmic(arr2):
    low=0
    high=len(arr2)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid-1]>arr[mid]<arr[mid+1]:
            return mid+1
        elif arr[mid-1]<arr[mid]<arr[mid+1]:
            low=mid+1
        else:
            high=mid-1





arr=list(map(int,input().split()))
# arr.index(min(arr)) TODO: although this will give the correct result but we should try to implement our logic first then use inbuilt function
print(count_rotation_linear(arr))
print(count_rotation_logrithmic(arr))
'''
3 4 5 6 1 2
ans 4
2 3 4 5 6 1
'''