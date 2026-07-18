class Solution:
    def gcd(self,a,b):
            while b:
                a,b=b,a%b
            return a
    def findGCD(self, nums: List[int]) -> int:
        mini=maxi=nums[0]
        for i in nums:
            mini=min(mini,i)
            maxi=max(maxi,i)
        return self.gcd(mini,maxi)