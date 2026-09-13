# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #2 trees are same if their childrens are same.
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        pl=p.left
        pr=p.right
        ql=q.left
        qr=q.right
        return self.isSameTree(pl,ql) and self.isSameTree(pr,qr)