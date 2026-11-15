class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd=0
        even=1
        pre=0
        ans=0
        mod=10**9+7
        for i in arr:
            pre+=i
            if pre%2==0:
                ans=(ans+odd)%mod
                even+=1
            else:
                ans=(ans+even)%mod
                odd+=1
        return ans