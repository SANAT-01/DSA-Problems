class Solution:
    def convert(self, s: str, r: int) -> str:
        if r == 1:
            return s
        l = ["" for i in range(r)]
        flag = 0
        idx = 0
        for i in range(len(s)):
            if idx >= r:
                flag = 1
                idx -= 2
            if idx < 0 :
                flag = 0
                idx += 2

            # print(idx)
            l[idx] += s[i]
            if not flag:
                idx += 1
            else:
                idx -= 1
        
        # print(l)
        return "".join(l)