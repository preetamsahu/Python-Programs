import math
N=int(input())
def isprime(N):
    if N==0:
        return 0
    elif N==1:
        return 0
    elif N==2:
        return 1
    else:
        for i in range(2,int(math.sqrt(N))+1):
            if N%i==0:
                return 0
        return 1
i=2
while 1:
    if isprime(i) and isprime(N-i):
        print(i,N-i)
        break
    i+=1

