class Solution(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numset:
                length = 1
                while (n + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest
    
a = Solution()
print(a.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))