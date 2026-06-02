class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        c = 0
        curr = -float('inf')
        for st, end in intervals:
            if st < curr:
                c += 1
            else:
                curr = end
        return c