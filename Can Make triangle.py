#TODO:'''Problme is solved'''
N=int(input())
arr=list(map(int,input().split()))
ans=[0]*(N-2)
for i in range(len(arr)-2):
    if (arr[i] + arr[i + 1]) > arr[i + 2] and (arr[i] + arr[i + 2]) > arr[i + 1] and (arr[i + 1] + arr[i + 2]) > arr[i]:
        ans[i] = 1
    else:
        ans[i] = 0
print(ans)
'''
4
1 2 2 4
ans=[1,0]

5
2 10 2 10 2
ans=[0 1 0]

9
2 3 10 5 9 2 2 10 3
ans=[0 0 1 0 0 0 0]
'''



