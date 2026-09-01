class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thres: int) -> int:
        adj=defaultdict(list)
        for i,j,d in edges:
            adj[i].append((j,d))
            adj[j].append((i,d))
        def traverse(s):
            seen=set([s])
            dist=[float('inf')]*n
            dist[s]=0
            q=collections.deque([(s,0)])
            while q:
                node,t=q.popleft()
                for ng,d in adj[node]:
                    if t+d<dist[ng] or ng not in seen:
                        if t+d<=thres:
                            seen.add(ng)
                            q.append((ng,d+t))
                        dist[ng]=d+t
            return len(seen)-1
        mini=float('inf')
        ans=[]
        for i in range(n):
            res=traverse(i)
            if mini>=res:
                ans.append(i)
                mini=res
        return ans[-1]