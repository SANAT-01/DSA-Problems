class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=0
        n=len(s)
        maxi=0
        while i<n:
            arr=s[:i+1]
            if arr==arr[::-1]:
                maxi=i+1
            i+=1
        print(maxi)
        return s[maxi:][::-1]+s