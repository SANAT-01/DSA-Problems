class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n:
            prod=1
            x=n
            while x:
                rem=x%10
                x//=10
                prod*=rem
            if prod%t==0:
                break
            n+=1
        return n