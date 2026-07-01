from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        safeness = [[-1] * n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safeness[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and safeness[nx][ny] == -1:
                    safeness[nx][ny] = safeness[x][y] + 1
                    queue.append((nx, ny))

        heap = [(-safeness[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while heap:
            safe, x, y = heapq.heappop(heap)
            safe = -safe

            if x == n-1 and y == n-1:
                return safe

            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    new_safe = min(safe, safeness[nx][ny])
                    heapq.heappush(heap, (-new_safe, nx, ny))

        return 0