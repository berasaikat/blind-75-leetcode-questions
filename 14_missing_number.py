class Solution(object):
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        return result
    
a = Solution()
print(a.missingNumber([3,0,1]))
print(a.missingNumber([0,1]))
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))

'''
Another solution using `XOR` operator
class Solution(object):
    def missingNumber(self, nums):
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result
'''