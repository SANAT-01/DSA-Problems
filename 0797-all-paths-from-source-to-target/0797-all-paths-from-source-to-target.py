class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(graph)
        def dfs(node,arr):
            if node==n-1:
                ans.append(arr)
                return
            for ng in graph[node]:
                dfs(ng,arr+[ng])
        dfs(0,[0])
        return ans