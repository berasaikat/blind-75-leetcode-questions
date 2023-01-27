class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(prices[right] - prices[left], max_profit)
            else:
                left = right
            right += 1
        return max_profit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))