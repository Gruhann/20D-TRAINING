# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def preorderTraversal(self, root):
#         l=[]
#         def preorder(root):
#             if root==None:
#                 return
#             l.append(root.val)
#             preorder(root.left)
#             preorder(root.right)
#         preorder(root)
#         return l
# # a=TreeNode()
# # o1=a.__init__(10)
# # o1.left=a.__init__(20)
# # o1.right=a.__init__(30)
# # print(a.preorderTraversal(o1))

class node:
    def _init_(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    print(root.val)#preorder
    printing(root.left)
    #print(root.val) #inorder
    printing(root.right)
    #print(root.val) #postorder
root=node(1)
root.left=node(2)
root.right=node(3)
printing(root)