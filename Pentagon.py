for i in range(5,0,-1):
    for j in range(i):
        print(" ",end=" ")
    print("*",end="")
    for j in range(2*(5-i)):
        print(" ",end=" ")
    if i!=5:
        print("*")
    else:
        print()
for i in range(1,6):
    for j in range(i):
        print(" ",end=" ")
    print("*",end="")
    for j in range(2*(5-i)):
        print(" ",end=" ")
    if i!=5:
        print("*")
    else:
        print()