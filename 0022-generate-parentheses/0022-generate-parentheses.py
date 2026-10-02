class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(o,c):
            if c==o and c==n:
                res.append("".join(stack))
                return
            if o<n:
                stack.append('(')
                back(o+1,c)
                stack.pop()
            if c<o:
                stack.append(')')
                back(o,c+1)
                stack.pop()

        back(0,0)
        return res