class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        n=len(s)
        def solve(x,i,cnt,l):
            if i==n:
                return
            if cnt==3:
                if int(s[l:])<=255 and (s[l]!='0' or l==n-1):
                    ans.append(x+s[l:])
                return
            if int(s[l:i+1])<=255 and (s[l]!='0' or l==i):
                solve(x+s[l:i+1]+'.',i+1,cnt+1,i+1)
            else:
                return
            solve(x,i+1,cnt,l)
            return
        solve("",0,0,0)
        return ans