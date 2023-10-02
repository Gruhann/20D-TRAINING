class node:
    def __init__(self, x):
        self.data=x
        self.next=None 
class LinkedList():
    def __init__(self):
        self.head=None
    def create(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def addFront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

b=LinkedList()
b.create(20)
b.create(30)
b.addFront(10)
b.display()