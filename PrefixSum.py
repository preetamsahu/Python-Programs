q=int(input())#Number of query
for _ in range(q):
    l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sum=[arr[0]]
    for i in range(1,len(arr)):
        x=prefix_sum[i-1]+arr[i]
        prefix_sum.append(x)
    print(prefix_sum,prefix_sum[])
