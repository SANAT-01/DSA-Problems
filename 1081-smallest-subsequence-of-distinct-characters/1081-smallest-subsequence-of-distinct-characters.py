class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt=Counter(s)
        stack=[]
        visited=set()
        for c in s:
            cnt[c]-=1
            if c in visited:
                continue
            while stack and stack[-1]>c and cnt[stack[-1]]:
                visited.remove(stack.pop())
            visited.add(c)
            stack.append(c)
        return "".join(stack)