'''
you are given an unsorted array and an key you need to find two pair, sum of them equal to given number
'''
number=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    complement=number-arr[i]
    if complement in arr:
        print(complement,arr[i])
        break
'''
17
1 2 3 2 1 3 6 4 2 4 2 1 10 7
'''