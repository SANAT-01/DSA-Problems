class Solution(object):
    def magicalString(self, n):
        ans=[1,2,2]
        i=2
        while len(ans)<n:
            ans+=[3-ans[-1]]*ans[i]
            i+=1
        return ans[:n].count(1)