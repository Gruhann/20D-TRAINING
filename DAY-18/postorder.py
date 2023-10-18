# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def preorderTraversal(self, root):
        l=[]
        def preorder(root):
            if root==None:
                return
            
            preorder(root.left)
            preorder(root.right)
            l.append(root.val)
        preorder(root)
        return l
# a=TreeNode()
# o1=a.__init__(10)
# o1.left=a.__init__(20)
# o1.right=a.__init__(30)
# print(a.preorderTraversal(o1))