class Solution:
    def removeCoveredIntervals(self, i: List[List[int]]) -> int:
        i.sort()
        start=i[0][0]
        end=i[0][1]
        cnt=0
        for j in i[1:]:
            if j[1]>end:
                if j[0]>start:
                    cnt+=1
                start,end=j
            else:
                continue
        return cnt+1