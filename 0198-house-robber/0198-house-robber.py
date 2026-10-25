class Solution:
    def rob(self, nums: List[int]) -> int:
        xsum,ysum=0,0
        for i in nums:
            new_ysum=xsum+i
            maxi=max(xsum,ysum)
            xsum,ysum=maxi,new_ysum
        return max(xsum,ysum)