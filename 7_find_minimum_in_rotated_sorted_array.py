class Solution(object):
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right)//2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return result

a = Solution()
print(a.findMin([3,4,5,1,2]))
print(a.findMin([4,5,6,7,0,1,2]))
print(a.findMin([11,13,15,17]))