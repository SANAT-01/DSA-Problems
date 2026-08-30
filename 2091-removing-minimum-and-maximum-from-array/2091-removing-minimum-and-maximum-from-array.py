class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))
        if mini>maxi:
            mini,maxi=maxi,mini
        fow=maxi+1
        back=len(nums)-mini
        res1=min(fow,back)
        res2=mini+1+len(nums)-maxi
        return min(res1,res2)