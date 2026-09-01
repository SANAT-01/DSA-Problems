import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj=defaultdict(list)
        for i,j,d in edges:
            self.adj[i].append((j,d))
        self.n=n

    def addEdge(self, edge: List[int]) -> None:
        i,j,d=edge
        self.adj[i].append((j,d))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist=[float('inf')]*self.n
        dist[node1]=0
        q=[(0,node1)]
        while q:
            d,node=heapq.heappop(q)
            if node == node2:
                return d
            if d > dist[node]:
                continue
            for ng,t in self.adj[node]:
                if d+t<dist[ng]:
                    dist[ng]=d+t
                    heapq.heappush(q,(d+t,ng))
        return dist[node2] if dist[node2]!=float('inf') else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)