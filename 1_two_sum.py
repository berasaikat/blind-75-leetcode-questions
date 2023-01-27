class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        HashMap = {}
        for i, n in enumerate(nums):
            if target - n in HashMap:
                return [HashMap[target - n], i]
            HashMap[n] = i
        return

a = Solution()
print(a.twoSum([2,7,11,15], 9))
print(a.twoSum([3,2,4], 6))
print(a.twoSum([3, 3], 6))