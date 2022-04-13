R=int(input())
a,b,c=map(int,input().split())
cnt=0
def cutrow(n,a,b,c):
    if n==0:
        return 0
    elif n<0:
        return -1
    res=max(cutrow(n-a, a, b, c),cutrow(n-b, a, b, c), cutrow(n-c, a, b, c))
    if res==-1:
        return -1
    else:
        return res+1

print(cutrow(R,a,b,c))