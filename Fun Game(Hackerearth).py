n=int(input())
arr=list(map(int,input().split()))
A=arr
B=list()
for i in A:
    B.append(i)
output=list()
while 1:
    if len(A) == 0 or len(B) == 0:
        break
    elif A[0] > B[-1]:
        B.pop(-1)
        output.append(1)
    elif A[0] < B[-1]:
        output.append(2)
        A.pop(0)
    else:
        output.append(0)
        A.pop(0)
        B.pop(-1)
# while True:
#     print("HELLO")
#     if len(A)==0 or len(B)==0:
#         break
#     elif A[i]>B[j]:
#         B.pop(j)
#         j=j-1
#         output.append(1)
#     elif A[i]<B[j]:
#         output.append(2)
#         A.pop(i)
#     else:
#         output.append(0)
#         A.pop(i)
#         B.pop(j)
#         j-=1
print(output,len(output))
# while 1:
#     if j==-1 or i==n:
#         break
#     if arr[i]>arr[j]:
#         output.append(1)
#         j-=1
#     elif arr[i]<arr[j]:
#         output.append(2)
#         i+=1
#     else:
#         output.append(0)
#         i+=1
#         j-=1
