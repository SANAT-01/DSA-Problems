class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt=[-1]*3
        ans=0
        for i in range(len(s)):
            cnt[ord(s[i])-ord('a')]=i
            ans+=1+min(cnt)
        return ans