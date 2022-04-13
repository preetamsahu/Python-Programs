value=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    print(i+1,arr[i])
sum=arr[0]
i=0
ans=[]
j=1
while j<=len(arr):

    if sum==value:
        ans.append(i+1)
        ans.append(j)
        break

    if sum<value:
        sum = sum + arr[j]
        j += 1
    elif sum>value:
        sum=sum-arr[i]
        i+=1
    print(sum, i + 1, j)

print(ans)
'''
468
135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134
12
1 2 3 7 5
'''