class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=even=0
        for i in range(1,n+1):
            odd+=i*2-1
            even+=i*2
        ans=0
        while even!=0:
            odd,even=even,odd%even
        return odd