class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], m: int) -> int:
        adj=collections.defaultdict(dict)
        for i,j,t in edges:
            adj[i][j]=adj[j][i]=t
        def dfs(node,visited,rem):
            maxi=0
            if node==0:
                maxi=sum(values[i] for i in visited)
            for ng in adj[node]:
                if adj[node][ng]<=rem:
                    maxi=max(maxi,dfs(ng,visited|{ng},rem-adj[node][ng]))
            return maxi
        return dfs(0,{0},m)