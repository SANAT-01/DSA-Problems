class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt=1
        for i in nums:
            if i>k*cnt:
                return k*cnt
            elif i==k*cnt:
                cnt+=1
        return k*cnt