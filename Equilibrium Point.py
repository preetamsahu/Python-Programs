arr=list(map(int,input().split()))
i=0
j=len(arr)-1
if len(arr)==1:
    print(1)
else:
    prifix_front=[arr[0]]
    prifix_back=[0 for i in range(len(arr))]
    prifix_back[len(arr)-1]=arr[len(arr)-1]
    for i in range(1,len(arr)):
        x=prifix_front[i-1]+arr[i]
        prifix_front.append(x)
    for i in range(len(arr)-2,-1,-1):
        prifix_back[i]=prifix_back[i+1]+arr[i]
    i=0
    j=len(arr)-1
    while i<j:
        if prifix_front[i]==prifix_back[j] and i+2==j:
            print("True",i+2)
            break
        else:
            if prifix_front[i]>prifix_back[j]:
                j-=1
            else:
                i+=1
    print(-1)
print(prifix_front,prifix_back)
"""
1
1
"""