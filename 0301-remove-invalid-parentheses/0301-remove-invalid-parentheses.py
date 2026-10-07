from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(st):
            bal = 0
            for ch in st:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        ans=[]
        q=deque([s])
        visited=set([s])
        while q:
            curr=q.popleft()
            if isValid(curr):
                ans.append(curr)
                continue
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                val=curr[:i]+curr[i+1:]
                if not ans and val not in visited:
                    visited.add(val)
                    q.append(val)
        return ans