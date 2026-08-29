class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], l: int) -> List[int]:
        n=len(nums)
        group=[]
        gmap={}
        for i in sorted(nums):
            if not group or i-group[-1][-1]>l:
                group.append([])
            group[-1].append(i)
            gmap[i]=len(group)-1
        itr=[iter(x) for x in group]
        for idx in range(n):
            nums[idx]=next(itr[gmap[nums[idx]]])
        return nums