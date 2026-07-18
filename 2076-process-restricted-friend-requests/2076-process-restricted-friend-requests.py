from typing import List

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        ans = []
        for u, v in requests:
            pu, pv = find(u), find(v)
            if pu == pv:
                ans.append(True)
                continue
            blocked = False
            for x, y in restrictions:
                px, py = find(x), find(y)
                if {px, py} == {pu, pv} or \
                   (px == pu and py == pv) or \
                   (px == pv and py == pu):
                    blocked = True
                    break
            if blocked:
                ans.append(False)
            else:
                union(u, v)
                ans.append(True)
            # print(parent)
        return ans