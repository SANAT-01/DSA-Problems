class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        cnt=1
        dp[0]=0
        while cnt*cnt<=n:
            sq=cnt*cnt
            for i in range(sq,n+1):
                dp[i]=min(dp[i-sq]+1,dp[i])
            cnt+=1
        return dp[-1]