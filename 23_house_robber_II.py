class Solution(object):
    def rob(self, nums: list[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0
            # [..., rob1, rob2, n, ...]
            for n in nums:
                rob1, rob2 = rob2, max(n+rob1, rob2)
            return rob2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
    
a = Solution()
print(a.rob([2,3,2]))
print(a.rob([1,2,3,1]))
print(a.rob([1,2,3]))