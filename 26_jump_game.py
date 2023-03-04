class Solution(object):
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal: goal = i
        return goal == 0
    
a = Solution()
print(a.canJump([2,3,1,1,4]))
print(a.canJump([3,2,1,0,4]))

'''
The above is a greedy approach.
We can do this by brute force DP approach too.
Code:
class Solution(object):
    def canJump(self, nums):
        def dfs(ind, memo):
            if ind in memo:
                return memo[ind]
            if ind >= len(nums)-1:
                return True 
            if nums[ind] == 0:
                return False
            for steps in range(nums[ind], 0, -1):
                goTo = ind + steps
                if dfs(goTo, memo):
                    memo[ind] = True
                    return True
            memo[ind] = False
            return False
        return dfs(0, {})
'''