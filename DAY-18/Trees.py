
def node(self,val):
    self.val=0
    self.left=None
    self.right=None
def printing(root):
    if root.val==0:
        return 
    print(root.val)
    printing(root.left)
    printing(root.right)
def dfsTraversal(self,root):
    q=[]
    q.append(root)
    while q:
        a=q.pop(0)
        print(a.val)
        if a.left:
            q.append(a.left)
        if a.right:
            q.append(a.right)
root=node(1)
root.left=node(2)
root.right=node(3)