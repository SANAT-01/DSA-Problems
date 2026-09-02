# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, des: List[List[int]]) -> Optional[TreeNode]:
        nodes={}
        hasParent={}
        for p,c,l in des:
            if p not in nodes:
                nodes[p]=TreeNode(p)
            if c not in nodes:
                nodes[c]=TreeNode(c)
            if l:
                nodes[p].left=nodes[c]
            else:
                nodes[p].right=nodes[c]
            hasParent[c]=True
            if p not in hasParent:
                hasParent[p]=False
        for i in hasParent:
            if not hasParent[i]:
                return nodes[i]
        return