class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = [[False] * n for _ in range(m)]
        def traverse(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1 or arr[i][j]:
                return True
                
            arr[i][j] = True
            t=traverse(i,j-1)
            l=traverse(i-1,j)
            r=traverse(i,j+1)
            b=traverse(i+1,j)
            return t and b and l and r
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not arr[i][j]:
                    if traverse(i, j):
                        cnt += 1
        return cnt