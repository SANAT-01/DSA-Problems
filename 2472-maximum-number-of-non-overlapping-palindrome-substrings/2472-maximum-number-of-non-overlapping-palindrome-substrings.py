class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        i=j=0
        ans=0
        while i<n:
            while j<n:
                val=s[i:j+1]
                if j-i+1>=k and val==val[::-1]:
                    ans+=1
                    i=j+1
                    j=i
                    break
                j+=1
                if j-i>k:
                    i+=1
                    j=i
                    break
            if j>=n:
                i+=1
                j=i
        return ans