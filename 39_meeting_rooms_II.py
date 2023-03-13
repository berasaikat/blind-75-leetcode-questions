# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1
        return min_rooms
    
a = Solution()
print(a.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(a.minMeetingRooms([[7,10],[2,4]]))
    
'''
Alternate Approach:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []  # Store end times of each room
        for start, end in sorted(intervals):
            if minHeap and start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
'''