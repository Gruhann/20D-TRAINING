#circular linkedlist
class node:
    def _init_(self,z):
        self.data=z;
        self.next=None
        self.prev=None
class dll:
    def _init_(self):
        self.head=None
        self.tail=None
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=node(x)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
            self.tail.next=self.head
            self.head.prev=self.tail
    def delete_beg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.tail.next=self.head
        self.head.prev=self.tail
    def delete_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
        self.head.prev=self.tail
    def traversal(self):
        print(self.head.data,end="-->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.data,end="-->")
            temp=temp.next
a=dll()
a.add_front(10)
a.add_front(20)
a.add_front(30)
a.add_end(40)
a.delete_beg()
a.delete_end()
a.traversal()