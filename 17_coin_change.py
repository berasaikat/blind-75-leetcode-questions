class Solution(object):
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amounts in range(1, amount+1):
            for coin in coins:
                if (amounts - coin) >= 0:
                    dp[amounts] = min(dp[amounts], 1+dp[amounts - coin])
        return dp[amount] if dp[amount] != amount+1 else -1
    
a = Solution()
print(a.coinChange([1,2,5], 11))
print(a.coinChange([2], 3))
print(a.coinChange([1], 0))