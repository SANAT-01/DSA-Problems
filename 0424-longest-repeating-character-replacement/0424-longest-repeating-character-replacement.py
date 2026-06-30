class Solution(object):
    def characterReplacement(self, s, k):
        ans=0
        maxi=0
        cnt={}
        j=0
        for i in range(len(s)):
            cnt[s[i]]=cnt.get(s[i],0)+1
            maxi=max(maxi,cnt[s[i]])
            while i-j+1-maxi>k:
                cnt[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans