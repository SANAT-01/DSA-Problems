class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans=0
        for i in arr:
            if i>ans:
                ans+=1
        return ans