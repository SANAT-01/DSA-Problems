class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        i=j=0
        dic={}
        ans=0
        while j<n:
            if s[j] not in dic:
                dic[s[j]]=1
                j+=1
            elif s[j] in dic and dic[s[j]]<2:
                dic[s[j]]+=1
                j+=1
            else:
                dic[s[i]]-=1
                i+=1
            ans=max(ans,j-i)
        return ans