class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        dist=[float('inf')]*n
        for i,j,d in times:
            adj[i].append((j,d))
        q=[(k,0)]
        seen=set([k])
        dist[k-1]=0
        while q:
            node,t=q.pop()
            for ng,d in adj[node]:
                if d+t<dist[ng-1] or ng not in seen:
                    seen.add(ng)
                    q.append((ng,d+t))
                    dist[ng-1]=d+t
        return max(dist) if max(dist)!=float('inf') else -1