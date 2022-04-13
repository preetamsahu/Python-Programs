class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Linked_list:
    def __init__(self):
        self.start=None
        self.index=0

    def InsertAtLast(self,item):
        newnode=node(item)
        if self.start==None:
            self.start=newnode
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=newnode
            newnode.next=None

    # def InsertAtBeginning(self,item):
    #     newnode=node(item)
    #
    def display(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data,end=" ")
            ptr=ptr.next
        print()
l1=Linked_list()
l1.InsertAtLast(12)
l1.InsertAtLast(8)
l1.InsertAtLast(3)
l1.InsertAtLast(2)
l1.InsertAtLast(4)
print(l1.start.data)
l1.display()