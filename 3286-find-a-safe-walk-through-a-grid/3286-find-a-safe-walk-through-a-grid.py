from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        m,n=len(grid),len(grid[0])
        visited=[[-1]*n for _ in range(m)]
        h=h-grid[0][0]
        if h<1:
            return False
        queue = deque([(0, 0, h)])
        while queue:
            i,j,sh=queue.popleft()
            if i == m-1 and j == n-1:
                return h >= 1
            for dx,dy in dir:
                di,dj=dx+i,dy+j
                if 0<=di<m and 0<=dj<n:
                    nh=sh-grid[di][dj]
                    if nh>=1 and nh>visited[di][dj]:
                        visited[di][dj]=nh
                        queue.append([di,dj,nh])
        return False