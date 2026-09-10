class Solution:
    def leftmostBuildingQueries(self, A, queries):
        def cmp(a, b):
            return (a > b) - (a < b)
        que = [[] for a in A]
        h = []
        res = [-1] * len(queries)
        for qi, (i, j) in enumerate(queries):
            if cmp(i, j) == cmp(A[i], A[j]):
                res[qi] = max(i, j)
            else:
                que[max(i, j)].append([max(A[i], A[j]), qi])
        for i, a in enumerate(A):
            while h and h[0][0] < a:
                res[heappop(h)[1]] = i
            for q in que[i]:
                heappush(h, q)
        return res