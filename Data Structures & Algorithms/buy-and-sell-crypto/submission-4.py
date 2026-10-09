class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0
        for price in prices:
            min_profit = min(min_profit, price)
            profit = price - min_profit
            max_profit = max(profit, max_profit)
        return max_profit