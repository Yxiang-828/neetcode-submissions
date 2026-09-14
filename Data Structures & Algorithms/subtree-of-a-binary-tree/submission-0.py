# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def match(node,subRoot):
            if(not node and not subRoot):
                return True
            if (not node and subRoot) or (not subRoot and node) or (node.val!=subRoot.val):
                return False
            return match(node.left, subRoot.left) and match(node.right, subRoot.right)
        def dfs(root):
            if not root:
                return False
            if match(root,subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root) 