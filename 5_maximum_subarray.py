class Solution(object):
    def maxSubArray(self, nums: list[int]) -> list[int]:
        max_so_far = nums[0]
        max_ending_here = 0
        for n in nums:
            max_ending_here += n
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([1]))
print(a.maxSubArray([5,4,-1,7,8]))