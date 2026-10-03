class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        maxi=0
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                stk.append(i)
            else:
                stk.pop()
                if stk==[]:
                    stk.append(i)
                else:
                    maxi=max(maxi,i-stk[-1])
        return maxi