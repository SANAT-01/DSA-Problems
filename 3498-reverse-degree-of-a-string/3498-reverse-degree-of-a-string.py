class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for idx,i in enumerate(s):
            ordi=ord(i)-ord('a')
            ans+=(26-ordi)*(idx+1)
        return ans