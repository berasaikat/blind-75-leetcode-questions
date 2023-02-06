class Solution(object):
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
    
a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(a.lengthOfLIS([0,1,0,3,2,3]))
print(a.lengthOfLIS([7,7,7,7,7,7,7]))