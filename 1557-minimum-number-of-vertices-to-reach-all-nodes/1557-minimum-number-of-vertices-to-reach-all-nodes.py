from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        deg=[0]*n
        for i,j in edges:
            deg[j]+=1
        return [idx for idx,i in enumerate(deg) if i==0]