from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def traverse(node):
            queue=[node]
            visited=set()
            visited.add(node)
            while queue:
                node=queue.pop()
                for ng in adj[node]:
                    if ng not in visited:
                        queue.append(ng)
                        visited.add(ng)
            return visited
        seen=[]
        ans=0
        for i in range(n):
            if i not in seen:
                arr=traverse(i)
                sm=0
                lg=len(arr)-1
                for node in arr:
                    sm+=len(adj[node])
                if lg*(lg+1)//2==sm//2:
                    ans+=1
                seen.extend(arr)
        return ans