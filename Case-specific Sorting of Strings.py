s=input()
lower=[0 for i in range(26)]
upper=[0 for i in range(26)]
lst=list(s)
for i in s:
    if i.isupper():
        upper[ord(i)-ord('A')]+=1
    else:
        lower[ord(i)-ord('a')]+=1
pos=0
low=0
high=0
print(lower,upper)
while pos<len(s):
    if lst[pos].islower():
        if lower[low]==0:
            while lower[low]<=0:
                low+=1
        lst[pos]=chr(ord('a')+low)
        lower[low]-=1
        pos+=1
    else:
        if upper[high]==0:
            while upper[high]<=0:
                high+=1
        lst[pos]=chr(ord('A')+high)
        upper[high]-=1
        pos+=1
lst="".join(lst)
print(lst)