class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        k=min(k,len(nums))
        for i in range(min(len(nums),k+1)):
            d[nums[i]]=d.get(nums[i],0)+1
            if d[nums[i]]>1:
                return True
        i,j=0,k+1
        while j<len(nums):
            d[nums[i]]=d.get(nums[i],0)-1
            d[nums[j]]=d.get(nums[j],0)+1
            if d[nums[j]]>1:
                return True
            i+=1
            j+=1
        return False