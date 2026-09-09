class Solution:
    def countCommas(self, n):
        if n<1000:
            return 0
        ans=0
        start=1000
        while start<=n:
            ans+=n-start+1
            start*=1000
        return ans