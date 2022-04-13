from collections import defaultdict
from numpy import np
arr=list(map(int,input().split()))
aay=np.array([1])

# N=len(arr)
#
# def getnum():
#     return 0
# dictt=defaultdict(getnum)
# for i in range(len(arr)):
#     dictt[arr[i]]+=1
# ans=[]
# for i in dictt:
#     if dictt[i]>(N//2):
#         ans.append(i)
# if len(ans)==0:
#     print(-1)
# else:
#     print(ans)