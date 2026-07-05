class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp={}
        def solve(n):
            if n<=1:
                return "0"
            if n in dp:
                return dp[n]
            val=solve(n-1)
            x="".join('0' if i=='1' else '1' for i in val)
            ans=val + '1' + x[::-1]
            dp[n]=ans
            return dp[n]
        return solve(n)[k-1]