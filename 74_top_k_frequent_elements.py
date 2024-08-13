class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_list = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for number in nums:
            count_list[number] = 1 + count_list.get(number, 0)
        for number, count in count_list.items():
            frequency[count].append(number)
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result
                
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3], 2))
print(a.topKFrequent([1], 1))