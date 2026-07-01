class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=0
        n=len(s)
        maxi=0
        arr=''
        rev=''
        while i<n:
            arr=s[i]+arr
            rev+=s[i]
            if rev==arr:
                maxi=i+1
            i+=1
        return s[maxi:][::-1]+s