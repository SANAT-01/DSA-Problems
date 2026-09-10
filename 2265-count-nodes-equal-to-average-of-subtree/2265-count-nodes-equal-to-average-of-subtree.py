# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=[0]
        def traverse(node):
            if not node:
                return 0,0
            l,ln=traverse(node.left)
            r,rn=traverse(node.right)
            if node.val==int((l+r+node.val)//(ln+rn+1)):
                ans[0]+=1
            return node.val+l+r,ln+rn+1
        traverse(root)
        return ans[0]