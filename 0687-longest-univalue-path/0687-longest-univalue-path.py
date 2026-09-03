# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def dfs(node,p):
            if not node:
                return 0
            left=dfs(node.left,node.val)
            right=dfs(node.right,node.val)
            ans[0]=max(ans[0],left+right)
            return max(left,right)+1 if node.val==p else 0
        dfs(root,0)
        return ans[0]