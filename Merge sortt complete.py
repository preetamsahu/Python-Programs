arr=list(map(int,input().split()))
def MergeSort(arr):
    if len(arr)==1:
        return arr
    mid =len(arr)//2
    left=MergeSort(arr[:mid])
    right=MergeSort(arr[mid:])
    return Sort(left,right)
def Sort(arr1,arr2):
    sorted_list=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            sorted_list.append(arr1[i])
            i+=1
        else:
            sorted_list.append(arr2[j])
            j+=1
    while i<len(arr1):
        sorted_list.append(arr1[i])
        i+=1
    while j<len(arr2):
        sorted_list.append(arr2[j])
        j+=1
    return sorted_list

print(MergeSort(arr))
'''
1 3 5 7 9 10 -2 -1 0 2 4 6
'''