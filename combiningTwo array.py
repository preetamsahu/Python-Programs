a=[1,3,6,9]
b=[4,5,7,8,9,213]
combine_sorted=list()
i=j=k=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        combine_sorted.append(a[i])
        i+=1
    else:
        combine_sorted.append(b[j])
        j+=1
while i<len(a):
    combine_sorted.append(a[i])
    i+=1
while j<len(b):
    combine_sorted.append(b[j])
    j+=1
print(combine_sorted)