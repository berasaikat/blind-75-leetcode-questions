class Solution(object):
    def maxProduct(self, nums: list[int]) -> int:
        current_max = current_min = result = nums[0]
        for n in nums[1:]:
            current_max, current_min = max(current_max * n, current_min * n, n), min(current_max * n, current_min * n, n)
            result = max(result, current_max)
        return result

a = Solution()
print(a.maxProduct([2,3,-2,4]))
print(a.maxProduct([-2,0,-1]))