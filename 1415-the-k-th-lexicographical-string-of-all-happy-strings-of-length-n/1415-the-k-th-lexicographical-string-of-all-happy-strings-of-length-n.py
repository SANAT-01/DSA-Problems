class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strs: list[str] = self.generate_happy_strs(n)
        if len(happy_strs) < k:
            return ""
        else:
            return happy_strs[k-1]

    def generate_happy_strs(self, n: int):
        if n == 1:
            return ['a', 'b', 'c']

        smallOutput: list[str] = self.generate_happy_strs(n-1)
        ans = []
        for char in ['a', 'b', 'c']:
            for ele in smallOutput:
                if char != ele[0]:
                    ans.append(char + ele)
        return ans