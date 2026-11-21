class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        dic={}
        ans=0
        for i in nums:
            val=dic.get(i,0)
            ans+=val
            dic[i]=val+1
        return ans