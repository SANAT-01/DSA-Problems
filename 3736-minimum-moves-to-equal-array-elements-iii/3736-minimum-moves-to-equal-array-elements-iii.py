class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans=0
        maxi=max(nums)
        for i in nums:
            ans+=abs(i-maxi)
        return ans