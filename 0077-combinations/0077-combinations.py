class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def solve(arr,i,l):
            if l==k:
                ans.append(arr)
                return
            if i>n:
                return
            solve(arr+[i],i+1,l+1)
            solve(arr,i+1,l)
        solve([],1,0)
        return ans