class Solution:
    def numOfStrings(self, p: List[str], word: str) -> int:
        ans=0
        for i in p:
            if i in word:
                ans+=1
        return ans