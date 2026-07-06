class Solution:
    def decodeString(self, s: str) -> str:
        def solve(x):
            if x.isalpha():
                return x
            i,n=0,len(x)
            ans=''
            while i<n:
                while i<n and x[i].isalpha():
                    ans+=x[i]
                    i+=1
                cnt=0
                while i<n and x[i].isnumeric():
                    cnt=cnt*10+int(x[i])
                    i+=1
                cnt=cnt if cnt else 1
                sub=''
                b=0
                i+=1
                while i<n and (x[i]!=']' or b>0):
                    if x[i]=='[': b+=1
                    elif x[i]==']': b-=1
                    sub+=x[i]
                    i+=1
                # print(x,cnt,sub)
                ans+=cnt*solve(sub)
                # print(ans)
                i+=1
            return ans
        return solve(s)