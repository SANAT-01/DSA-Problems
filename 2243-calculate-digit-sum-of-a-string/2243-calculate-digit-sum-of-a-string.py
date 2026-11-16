class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            sub=''
            i=0
            sm=0
            while i<len(s):
                if i!=0 and i%k==0:
                    sub+=str(sm)
                    sm=0
                sm+=int(s[i])
                i+=1
            sub+=str(sm)
            s=sub
        return s