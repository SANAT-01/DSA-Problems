from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        mini=float('inf')
        queue=[1]
        visited=set()
        visited.add(1)
        adj=defaultdict(list)
        for i,j,d in roads:
            adj[i].append((j,d))
            adj[j].append((i,d))
        while queue:
            node=queue.pop()
            for ng,d in adj[node]:
                mini=min(mini,d)
                if ng not in visited:
                    visited.add(ng)
                    queue.append(ng)
        return mini