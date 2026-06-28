class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        def mergeCount(l,r):
            if l>=r:
                return 0
            mid=(l+r)//2
            cnt=mergeCount(l,mid)+mergeCount(mid+1,r)
            j=mid+1
            for i in range(l,mid+1):
                while j<=r and nums[i]>2*nums[j]:
                    j+=1
                cnt+=j-(mid+1)
            x,y=l,mid+1
            ans=[]
            while x<=mid and y<=r:
                if nums[x]<nums[y]:
                    ans.append(nums[x])
                    x+=1
                else:
                    ans.append(nums[y])
                    y+=1
            while x<=mid:
                ans.append(nums[x])
                x+=1
            while y<=r:
                ans.append(nums[y])
                y+=1
            nums[l:r+1]=ans
            return cnt
        return mergeCount(0,n-1)