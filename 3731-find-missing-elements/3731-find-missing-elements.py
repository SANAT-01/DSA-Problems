class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini,maxi=min(nums),max(nums)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                ans.append(i)
        return ans