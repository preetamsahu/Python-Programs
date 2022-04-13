import time
n,m=map(int,input().split())
s='.|.'
cnt=1
for i in range(n//2):
    print((s*cnt).center(m,'-'))
    time.sleep(0.3)
    cnt+=2
cnt-=2
print("WELCOME".center(m,'-'))
time.sleep(0.3)
for i in range(n//2):
    print((s*cnt).center(m,'-'))
    time.sleep(0.3)
    cnt-=2

#TODO: 57 17157 171