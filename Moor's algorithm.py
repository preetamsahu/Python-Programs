'''
This algorithm is used to find the majority element in the array that occur more than n//2 times.
basically it maintain the count var, that increase when previous element is same as current value if it is not and count==1 then we made count==0 and set majority element
as current value since majority element occurs n//2 times hence at the end maj var will contain the majority element
'''
arr=list(map(int,input().split()))
count=1
maj=arr[0]
for i in range(1,len(arr)):
    if maj==arr[i]:
        count+=1
    elif count>1:
        count-=1
    else:
        count=1
        maj=arr[i]
if count>1:
    print(maj)
else:
    print(-1)

