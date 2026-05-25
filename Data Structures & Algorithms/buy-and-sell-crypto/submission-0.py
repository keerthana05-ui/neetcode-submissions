class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        if len(prices) < 2:
            return 0
        for right in range(1, len(prices)):
            if prices[left]<prices[right]:
                current_profit = prices[right]-prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
        return max_profit