from collections import defaultdict
X=int(input())
def assign():
    return 0
numbers=list(map(int,input().split()))
for i in range(len(numbers)):
    numbers[i]=str(numbers[i])
cnt=0
dick=defaultdict(assign)
sett=list(set(numbers))
for i in sett:
    dick[i]=numbers.count(i)
X=str(X)
for i in range(len(X)):
    first=X[:i]
    second=X[i:]
    if first == second:
        cnt=cnt+dick[first]*(dick[first]-1)
    else:
        cnt=cnt+dick[first]*dick[second]
print(cnt)