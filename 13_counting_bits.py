class Solution(object):
    def countBits(self, n: int) -> list[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp

a = Solution()
print(a.countBits(2))
print(a.countBits(5))


'''
class Solution(object):
    def countBits(self, n: int) -> list[int]:
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i&1)
        return ans
'''