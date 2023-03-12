# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals[1:]):
            if interval.start < intervals[i].end:
                return False
        return True

a = Solution()
print(a.canAttendMeetings([[0,30],[5,10],[15,20]]))
print(a.canAttendMeetings([[7,10],[2,4]]))

# Runs on LeetCode but not been able to run on my local machine :(