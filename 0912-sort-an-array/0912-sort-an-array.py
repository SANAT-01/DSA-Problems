class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini,maxi=min(nums),max(nums)
        arr=[0]*(maxi-mini+1)
        for i in nums:
            arr[i-mini]+=1
        ans=[]
        for idx,i in enumerate(arr):
            if i:
                ans.extend([mini+idx]*i)
        return ans