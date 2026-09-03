class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini=nums1[0]
        hasOdd=False
        for i in nums1:
            if i%2==1:
                hasOdd=True
            mini=min(mini,i)
        if hasOdd and mini%2==0:
            return False
        return True