class Solution:
    def stoneGame(self, points: List[int]) -> bool:
        alice=bob=0
        i=0
        j=len(points)-1
        cnt=0
        while i<=j:
            val=None
            if points[i]<points[j]:
                val=points[j]
                j-=1
            else:
                val=points[i]
                i+=1
            alice+=val if cnt%2==0 else 0
            bob+=val if cnt%2!=0 else 0
        return alice>bob