class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maxi=[0]*n
        mini=[float('inf')]*n
        if n==1:
            return 0
        for i in range(n):
            if i==0:
                maxi[i]=nums[i]
                mini[-1]=nums[-1]
            else:
                maxi[i]=max(maxi[i-1],nums[i])
                mini[n-1-i]=min(mini[n-i],nums[n-1-i])
        for i in range(n):
            if maxi[i]-mini[i]<=k:
                return i
        return -1