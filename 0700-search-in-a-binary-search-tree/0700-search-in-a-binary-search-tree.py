# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node,t):
            if not node:
                return 
            if node.val==t:
                return node
            elif node.val>t:
                return traverse(node.left,t)
            else:
                return traverse(node.right,t)
        return traverse(root,val)