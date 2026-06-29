class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt=[0,0,0]
        i=j=0
        n=len(s)
        ans=0
        while j<n:
            if cnt[0]>0 and cnt[1]>0 and cnt[2]>0:
                ans+=n-j+1
                idx=ord(s[i])-ord('a')
                cnt[idx]-=1
                i+=1
            else:
                idx=ord(s[j])-ord('a')
                cnt[idx]+=1
                j+=1
            # print(cnt,ans,i,j)
        if cnt[0]>0 and cnt[1]>0 and cnt[2]>0:
            ans+=n-j+1
        idx=ord(s[i])-ord('a')
        cnt[idx]-=1
        i+=1
        while i<j and cnt[0]>0 and cnt[1]>0 and cnt[2]>0:
            ans+=1
            idx=ord(s[i])-ord('a')
            cnt[idx]-=1
            i+=1
        return ans