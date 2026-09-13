import numpy

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        cnt = defaultdict(int)
        best = 0
        for ax, ay in A:
            for bx, by in B:
                dx = bx - ax
                dy = by - ay
                cnt[(dx,dy)] += 1
                best = max(best, cnt[(dx,dy)])
        return best