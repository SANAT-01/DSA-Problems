class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            dic[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr