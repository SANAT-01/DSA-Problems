class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    break
            if grid[i][j]:
                break
        dir=[(-1,0),(0,-1),(1,0),(0,1)]
        queue=[(i,j)]
        visited[i][j]=True
        while queue:
            x,y=queue.pop()
            for ni,nj in dir:
                nx,ny=ni+x,nj+y
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny]==1 and not visited[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                    elif grid[nx][ny]==0:
                        ans+=1
                elif x==0 or y==0 or x==m-1 or y==n-1:
                    ans+=1
        return ans