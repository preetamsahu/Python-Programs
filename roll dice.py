from random import randint
print("Welcome to roll dice game")
print("To quit the game press any character then ENTER")
player1=input("Enter the name of 1st PLAYER ")
player2=input("Enter the name of 2nt PLAYER ")
x1=0
x2=0
c=1
while 1:
    if c==1:
        s=input("Start ")
        c+=1
    else:
        s=input()
    if s=="":
        z=randint(1,6)
        print(player1,"get",z,end=" ")
        x1+=z
        s=input()
        z = randint(1, 6)
        print(player2,"get",z,end=" ")
        x2+=z
    else:
        break
print(f"{player1} score is {x1}")
print(f"{player2} score is {x2}")
if x1==x2:
    print("TIE")
elif x1>x2:
    print(player1,"win",player2-player1)
else:
    print(player2,"win","by",player2-player1)