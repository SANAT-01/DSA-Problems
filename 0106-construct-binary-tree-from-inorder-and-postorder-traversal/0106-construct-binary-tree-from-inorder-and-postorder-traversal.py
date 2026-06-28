# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        m={v:idx for idx,v in enumerate(inorder)}
        pi=[len(inorder)-1]
        def recurr(inorder,postorder,pi,l,r,m):
            if l>r:
                return None
            val=postorder[pi[0]]
            node=TreeNode(val)
            pi[0]-=1
            idx=m[val]
            if l==r:
                return node
            node.right=recurr(inorder,postorder,pi,idx+1,r,m)
            node.left=recurr(inorder,postorder,pi,l,idx-1,m)
            return node
        return recurr(inorder,postorder,pi,0,len(inorder)-1,m)