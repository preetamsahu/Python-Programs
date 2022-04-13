A=list(map(int,input().split()))
X=int(input())
lst = []
for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
        lst.append([A[i] + A[j]])
for i in lst:
    complement = X - sum(i)
    print(sum(i),complement)
    if complement in A:
        print("True")
print("False")
'''
998 550 557 562 628 468 542 130 241
793
'''