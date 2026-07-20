class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, d: int) -> bool:
        adj=collections.defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        queue=[source]
        visited=set()
        visited.add(source)
        while queue:
            node=queue.pop()
            if node==d:
                return True
            for ng in adj[node]:
                if ng not in visited:
                    visited.add(ng)
                    queue.append(ng)
        return False