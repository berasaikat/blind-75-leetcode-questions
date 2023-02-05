class Solution(object):
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            one, two = one+two, one
        return one
    
a = Solution()
print(a.climbStairs(2))
print(a.climbStairs(3))