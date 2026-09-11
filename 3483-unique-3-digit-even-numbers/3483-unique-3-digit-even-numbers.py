class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = set()
        ans = 0
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if x not in vis:
                        vis.add(x)
                        ans += 1
        return ans