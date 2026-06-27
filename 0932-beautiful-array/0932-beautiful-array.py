class Solution:
    def beautifulArray(self, n):
        res=[1]
        while len(res)<=n:
            res=[2*i-1 for i in res] + [2*i for i in res]
        return [i for i in res if i<=n]