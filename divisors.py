from math import sqrt
N=int(input())
#findingg threes div
def no_divisors(n):
    div=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            div.append(i)
            div.append(n//i)
    print(n)
    div=set(div)
    # print(div)
    if len(div)==3:
        # print(n)
        return 1
    else:
        return 0
cnt=0
no_divisors(5)
for i in range(4,N+1):
    if no_divisors(i):
        cnt+=1

print(cnt)