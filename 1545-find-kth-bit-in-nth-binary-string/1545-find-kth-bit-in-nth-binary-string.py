class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n):
            if n<=1:
                return "0"
            val=solve(n-1)
            x="".join('0' if i=='1' else '1' for i in val)
            return val + '1' + x[::-1]
        return solve(n)[k-1]