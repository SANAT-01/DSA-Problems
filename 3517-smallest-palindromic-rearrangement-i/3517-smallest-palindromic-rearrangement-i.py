class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left = []
        mid = ""
        for c in sorted(count):
            left.append(c * (count[c] // 2))
            if count[c] % 2:
                mid = c
        left = "".join(left)
        return left + mid + left[::-1]