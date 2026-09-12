from bisect import bisect_left
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        interval_indices = {}
        for i, (l, r, w) in enumerate(intervals):
            tup = (l, r, w)
            if tup not in interval_indices:
                interval_indices[tup] = i
        sorted_intervals = sorted(interval_indices.keys())
        n = len(sorted_intervals)
        @lru_cache(None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0, []
            skip_w, skip_indices = dp(i + 1, remaining)
            l, r, w = sorted_intervals[i]
            next_i = bisect_left(sorted_intervals, (r + 1, -1, -1))
            next_w, next_indices = dp(next_i, remaining - 1)
            take_w = w + next_w
            take_indices = sorted(next_indices + [interval_indices[(l, r, w)]])
            if take_w > skip_w:
                return take_w, take_indices
            elif take_w < skip_w:
                return skip_w, skip_indices
            else:
                if take_indices < skip_indices:
                    return take_w, take_indices
                else:
                    return skip_w, skip_indices
        return dp(0, 4)[1]