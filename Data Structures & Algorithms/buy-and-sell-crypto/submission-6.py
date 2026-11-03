class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in prices:
            profit = i - min_price
            max_profit = max(max_profit, profit)
            min_price = min(i, min_price)
        return max_profit