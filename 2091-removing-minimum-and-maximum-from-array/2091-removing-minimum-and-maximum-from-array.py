class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mini=min(nums)
        maxi=max(nums)
        idx=[0,0]
        for i in range(n):
            if nums[i]==mini:
                idx[0]=i
            if nums[i]==maxi:
                idx[1]=i
        mini,maxi=idx
        if mini<=n//2 and maxi<=n//2:
            return max(mini,maxi)+1
        elif mini>=n//2 and maxi>=n//2:
            return n-min(maxi,mini)
        else:
            if mini>maxi:
                mini,maxi=maxi,mini
            ans=0
            if mini+1<n-maxi:
                return mini+1 + min(maxi-mini,n-maxi)
            else:
                return n-maxi + min(mini+1,maxi-mini)