for i in range(1,101):
    flag=True
    factor=list()
    if i==1:
        print(i)
    elif i==2:
        print(i)
    else:
        for j in range(1,(i)//2):
            if i%j==0:
                factor.append(i//j)
                factor.append(j)
    if len(factor)==2:
        print(i,factor)