class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newrow = [1] * n
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]
            row = newrow
        return row[0]
    
a = Solution()
print(a.uniquePaths(3,7))
print(a.uniquePaths(3,2))

'''
Alternate approach:
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
'''