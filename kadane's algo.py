arr=list(map(int,input().split()))
prv=max_sum=arr[0]
curr=0
j=0
p=0
tri=0
while j<len(arr):
    curr=curr+arr[j]

    max_sum=max(max_sum,curr)
    if curr<0:
        curr=0

    j+=1
print(max_sum)
'''
1 2 3 -2 5
'''