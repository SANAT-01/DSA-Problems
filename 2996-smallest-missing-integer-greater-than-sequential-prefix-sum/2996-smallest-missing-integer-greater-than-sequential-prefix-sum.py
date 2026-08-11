class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sm=nums[0]
        n=len(nums)
        i=1
        while i<n and nums[i]==nums[i-1]+1:
            sm+=nums[i]
            i+=1
        while True:
            if sm not in nums:
                return sm
            sm+=1
        return