from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        cntr=defaultdict(int)
        for i,j in edges:
            adj[i].append(j)
            cntr[i]+=1
            adj[j].append(i)
            cntr[j]+=1
        visited=[0]*n
        def traverse(node):
            if node not in adj:
                return True
            queue=[node]
            visited[node]=1
            ed=len(adj[node])
            nodes=1
            while queue:
                curr_node=queue.pop()
                for ng in adj[curr_node]:
                    if not visited[ng]:
                        queue.append(ng)
                        visited[ng]=1
                        ed+=cntr[ng]
                        nodes+=1
            return ed//2==nodes*(nodes-1)//2
        cnt=0
        for i in range(n):
            if not visited[i] and traverse(i):
                cnt+=1
        return cnt