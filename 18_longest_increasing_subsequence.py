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

'''
This is using patience sort that takes O(nlogn) time, where the previous dynamic approach runs on O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)
'''