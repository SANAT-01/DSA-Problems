class Solution:
    def longestPrefix(self, s: str) -> str:
        i,n=0,len(s)
        if n<=1:
            return ''
        x=y=''
        maxi=0
        while i<n-1:
            x+=s[i]
            y=s[n-i-1]+y
            if x==y:
                maxi=i
            i+=1
        if maxi==0:
            if s[0]!=s[-1]: return ''
        return s[:maxi+1]