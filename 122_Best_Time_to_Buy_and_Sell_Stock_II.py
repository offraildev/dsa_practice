from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        # whenever we book a profit, restart the buy counter and 
        # start booking the next profit
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            if profit > 0:
                max_profit += profit
                buy = prices[i]
        return max_profit
