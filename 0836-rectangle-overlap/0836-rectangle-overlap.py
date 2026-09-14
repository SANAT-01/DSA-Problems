class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=rec1
        x11,y11,x22,y22=rec2
        if x1==x2 or y1==y2 or x11==x22 or y11==y22:
            return False
        return not (
            x2<=x11 or
            x22<=x1 or
            y2<=y11 or
            y22<=y1
        )