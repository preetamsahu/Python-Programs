from time import sleep
s="**"
cnt=1
for i in range(8,0,-1):
    for j in range(i-1):
        print(" ",end=" ")
    # sleep(.5)
    print(s*cnt,end="")
    for j in range(2*(i-1)):
        print(" ",end=" ")
    print(s*cnt)
    cnt+=2
cnt-=2
for i in range(17):
    for j in range(i):
        print(" ",end=" ")
    # sleep(.5)
    print(s*cnt*2)
    cnt-=1