class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right - left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return water

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
print(a.maxArea([1,1]))