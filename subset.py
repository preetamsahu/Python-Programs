x=list(map(int,input().split()))
def subset(x,curr,lst,i):
    if i==len(x):
        curr.append(lst)
        return curr
    
    subset(x,curr,lst,i+1)
    curr.appends(x[i])
    subset(x,curr,lst)