def fibbo(n):
    if n==1:
        return n
    elif n==0:
        return n
    else:
        return fibbo(n-2)+fibbo(n-1)
for i in range(11):
    print(i,":",fibbo(i))