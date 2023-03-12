class Solution(object):
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
            else:
                res += 1
                prevend = min(prevend, end)
        return res
    
a = Solution()
print(a.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(a.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(a.eraseOverlapIntervals([[1,2],[2,3]]))

'''
Alternate Solution using endpoint of the intervals to sort them.
You can also initialize prevend to -inf (import math and use -math.inf) and iterate over the entire list instead of [1:].
class Solution(object):
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        res = 1
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevend:
                prevend = end
                res += 1
        return len(intervals) - res
'''