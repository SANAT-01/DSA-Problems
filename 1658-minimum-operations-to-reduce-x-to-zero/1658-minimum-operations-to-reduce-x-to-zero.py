class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        t,n = sum(nums)-x, len(nums)
        if t == 0:
            return n
        left, curr, maxi = 0,0,0
        for right, val in enumerate(nums):
            curr += val
            while left<=right and curr>t:
                curr -= nums[left]
                left += 1
            if t == curr:
                maxi = max(maxi, right-left+1)
        return n-maxi if maxi else -1