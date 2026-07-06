class Solution:
    def removeCoveredIntervals(self, i: List[List[int]]) -> int:
        i.sort()
        print(i)
        start=i[0][0]
        end=i[0][1]
        ans=[]
        for j in i[1:]:
            if j[1]>end:
                if j[0]>start:
                    ans.append([start,end])
                start,end=j
            else:
                continue
        ans.append([start,end])
        print(ans)
        return len(ans)