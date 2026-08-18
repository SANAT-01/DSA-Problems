class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        arr=[0]*n
        dic={}
        for i in range(k):
            dic[nums[i]]=dic.get(nums[i],0)+1
        for i in range(k):
            if dic[nums[i]]==1:
                arr[i]+=1
        i+=1
        while i<n:
            dic[nums[i-k]]-=1
            dic[nums[i]]=dic.get(nums[i],0)+1
            for j in range(i-k+1,i+1):
                if dic[nums[j]]==1:
                    arr[j]+=1
            i+=1
        rep={}
        for i in nums:
            rep[i]=rep.get(i,0)+1
        ans=-1
        for i in range(n):
            if arr[i]*rep[nums[i]]==1 or k==n:
                ans=max(ans,nums[i])
        return ans