import heapq
class MedianFinder(object):
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], []]
expected_output = [None, None, None, 1.5, None, 2.0]
actual_output = []

median_finder = None

for i in range(len(operations)):
    if operations[i] == "MedianFinder":
        median_finder = MedianFinder()
        actual_output.append(None)
    elif operations[i] == "addNum":
        median_finder.addNum(values[i][0])
        actual_output.append(None)
    elif operations[i] == "findMedian":
        result = median_finder.findMedian()
        actual_output.append(result)

# Compare actual output with expected output
print("Actual Output: ", actual_output)
print("Expected Output: ", expected_output)
print("Test Passed: ", actual_output == expected_output)

'''
import heapq
class MedianFinder(object):
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
'''