class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        sums=[0]*n
        for idx,i in enumerate(nums):
            j=i
            sm=0
            while j:
                sm+=j%10
                j=j//10
            sums[idx]=sm
        indices=list(range(n))
        indices.sort(key=lambda i: (sums[i],nums[i]))
        target=[0]*n
        for idx,i in enumerate(indices):
            target[i]=idx
        print(indices,target)
        visited=[False]*n
        cycles=0
        for i in range(n):
            if visited[i]:
                continue
            cycles+=1
            visited[i]=True
            j=target[i]
            while not visited[j]:
                visited[j]=True
                j=target[j]
        return n-cycles