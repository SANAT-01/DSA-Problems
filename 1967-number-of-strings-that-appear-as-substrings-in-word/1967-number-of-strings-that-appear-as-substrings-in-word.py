class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for p in patterns:
            for i in range(len(word) - len(p) + 1):
                j = 0
                while j < len(p) and word[i+j] == p[j]:
                    j += 1
                if j == len(p):
                    count += 1
                    break
        return count