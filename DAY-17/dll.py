#linkedlist
class node:
    def __init__(self,z):
        self.data=z;
        self.next=None
        self.prev=None
class list:
    def __init__(self):
        self.head=None
        self.tail=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            newnode=node(x)
            temp.next=newnode.prev
            newnode.next=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            temp=node(x)
            temp.next=self.head
            temp.prev=None
            self.head=temp 
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            temp=node(x)
            curr.next=temp
            temp.prev=curr
            temp.next=None
    def delete_beg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data
    def traversal(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
a=list()
a.creat(10)
a.creat(20)
a.creat(30)
a.add_front(70)
a.add_end(25)
a.delete_beg()
a.traversal()