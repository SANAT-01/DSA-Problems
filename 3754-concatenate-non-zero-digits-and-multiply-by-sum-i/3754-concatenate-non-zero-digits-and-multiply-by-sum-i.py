class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=0
        sm=0
        pow=0
        while n:
            r=n%10
            sm+=r
            if r>0:
                num=num+r*(10**pow)
                pow+=1
            n//=10
        print(num,sm)
        return num*sm