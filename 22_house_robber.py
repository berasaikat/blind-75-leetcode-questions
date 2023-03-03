class Solution(object):
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        # [..., rob1, rob2, i, ...]
        for i in nums:
            rob1, rob2 = rob2, max(i + rob1, rob2)
        return rob2
    
a = Solution()
print(a.rob([1,2,3,1]))
print(a.rob([2,7,9,3,1]))