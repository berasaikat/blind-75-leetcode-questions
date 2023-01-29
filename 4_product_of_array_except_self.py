class Solution(object):
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= postfix
            postfix *= nums[i]
        return arr

a= Solution()
print(a.productExceptSelf([1,2,3,4]))
print(a.productExceptSelf([-1,1,0,-3,3]))
