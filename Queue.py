Front=0
Rear=0
n=int(input("ENter the size of the Queue"))
Queue=[0]*n
def insert(item,N):
    global Front,Rear
    if Front==0 and Rear>N-1 or Front==Rear+1:#Size of the queue
        print(f"OverFlow condition {item} cann't inserted")
    elif Rear==N and Front!=0:
        Rear=0
        Queue[Rear]=item
        print(f"{item} is inserted --> ",end="")
        display(Queue)
        print()
        Rear += 1
    elif Front==0 and Rear<N:
        Queue[Rear]=item
        print(f"{item} is inserted --> ", end="")
        display(Queue)
        print()
        Rear+=1
def display(q):
    for i in q:
        print(i,end=" ")
def remove():
    global Front,Rear
    if Rear==Front:
        print("Underflow condition")
    else:
        print(f"{Queue[Front]} is deleted ",end=" ")
        Queue[Front]=0
        Front+=1
        for i in Queue:
            print(i,end=" ")
        print()

insert(13,n)
insert(2,n)
insert(3,n)
insert(6,n)
insert(7,n)
insert(8,n)
insert(9,n)
remove()
remove()
insert(12,n)
insert(5,n)
