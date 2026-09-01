import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], thres: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for ng, w in adj[node]:
                    if dist[node] + w < dist[ng]:
                        dist[ng] = dist[node] + w
                        heapq.heappush(heap, (dist[ng], ng))
            return sum(1 for j in range(n) if src != j and dist[j] <= thres)

        ans = -1
        mini = float('inf')
        for i in range(n):
            cnt = dijkstra(i)
            if cnt <= mini:
                mini = cnt
                ans = i
        return ans