class Solution:
    def highestPeak(self, w: List[List[int]]) -> List[List[int]]:
        queue=[]
        m,n=len(w),len(w[0])
        visited=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if w[i][j]==1: 
                    queue.append((i,j,0))
                    visited[i][j]=True
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        ans=[[0]*n for _ in range(m)]
        while queue:
            x,y,d=queue.pop(0)
            for di,dj in dir:
                dx,dy=di+x,dj+y
                if 0<=dx<m and 0<=dy<n and not visited[dx][dy]:
                    visited[dx][dy]=True
                    ans[dx][dy]=d+1
                    queue.append((dx,dy,d+1))
        print(ans)
        return ans