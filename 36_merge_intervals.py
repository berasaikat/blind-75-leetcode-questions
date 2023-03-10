class Solution(object):
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output
    
a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))
print(a.merge([[1,4],[4,5]]))