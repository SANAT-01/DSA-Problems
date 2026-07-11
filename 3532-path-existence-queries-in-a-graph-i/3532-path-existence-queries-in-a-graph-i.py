class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], d: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        for i in range(1, n):
            group[i] = group[i-1] if nums[i] - nums[i-1] <= d else group[i-1] + 1
        return [group[min(i,j)] == group[max(i,j)] for i, j in queries]