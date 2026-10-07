"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root=node.val
        dic={}
        queue=[node]
        visited=set()
        visited.add(node.val)
        while queue:
            node=queue.pop()
            if node.val not in dic:
                dic[node.val]=Node(node.val)
            for ng in node.neighbors:
                if ng.val not in dic:
                    dic[ng.val]=Node(ng.val)
                dic[node.val].neighbors.append(dic[ng.val])
                if ng.val not in visited:
                    queue.append(ng)
                    visited.add(ng.val)
        return dic[root]