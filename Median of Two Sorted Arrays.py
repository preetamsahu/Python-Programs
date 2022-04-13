arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
merged_arr=list()
l=len(arr1)+len(arr2)
l1=len(arr1)
l2=len(arr2)
if l%2==0:
    ind1=l//2-1
    ind2=l//2
else:
    ind=l//2
i=0
while 1:
   if arr1[i]<arr2[i]:
       mid=l1//2
