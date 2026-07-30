class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        rem=n%8
        div=n//8
        sm=div*(div+1)//2
        return 8*sm+(div+1)*rem