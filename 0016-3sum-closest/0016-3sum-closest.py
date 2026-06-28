class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
        nums.sort()
        n=len(nums)
        mini=float('inf')
        ans=0
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                val=nums[i]+nums[l]+nums[r]
                if abs(val-t)<mini:
                    mini=abs(val-t)
                    ans=val
                if mini==0:
                    return t
                if val>t:
                    r-=1
                else:
                    l+=1   
        return ans