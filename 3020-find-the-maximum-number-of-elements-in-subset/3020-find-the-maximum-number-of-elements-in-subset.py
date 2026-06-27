class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt={}
        for i in nums:
            cnt[i]=cnt.get(i,0)+1
        maxi=0
        for i in cnt:
            x=i
            l=0
            if i==1:
                maxi=max(maxi,cnt[i]-1 if cnt[i]%2==0 else cnt[i])
                continue
            while x in cnt and cnt[x]>=2:
                x=x**2
                l+=2 if x in cnt else 0
            l+=1
            maxi=max(maxi,l)
        return maxi