N=int(input())
arr=list(map(int,input()))
xXORy=arr[0]
for i in range(1,len(arr)):
    xXORy^=arr[i]
for i in range(1,N+1):
    xXORy^=i
buk1=[]#contain set
buk2=[] #contain not set
for i in arr:
    k=bin(i)
    if k[2]==1:
        buk1.append(i)
for i in range(1,N+1):
    k=bin(i)
