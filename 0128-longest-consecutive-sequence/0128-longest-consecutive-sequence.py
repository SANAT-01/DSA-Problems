class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set(nums)
        maxi=0
        for i in s:
            if i-1 not in s:
                curr=i
                l=1
                while curr+1 in s:
                    curr+=1
                    l+=1
                maxi=max(maxi,l)
        return maxi