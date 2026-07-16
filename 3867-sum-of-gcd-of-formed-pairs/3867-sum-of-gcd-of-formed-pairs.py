class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def solve(a,b):
            while b:
                a,b=b,a%b
            return a
        l=nums[0]
        arr=[]
        for i in nums:
            l=max(l,i)
            val=solve(i,l)
            arr.append(val)
        arr.sort()
        i=0
        j=len(arr)-1
        ans=0
        while i<j:
            ans+=solve(arr[i],arr[j])
            i+=1
            j-=1
        return ans