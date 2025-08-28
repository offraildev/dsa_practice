from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # single pointer
        max_profit = 0
        min_buy_price = prices[0]
        for sell_price in prices[1:]:
            min_buy_price = min(min_buy_price, sell_price)
            max_profit = max(max_profit, sell_price - min_buy_price)
        return max_profit

        # brute force
        # max_profit = 0
        # for i, a in enumerate(prices):
        #     for b in prices[i:]:
        #         max_profit = max(b-a, max_profit)
        # return max_profit

        # two pointers
        # if len(prices) <= 1:
        #     return 0
        # [1,2,4,2,5,7,2,4,9,0,9]: edge case for moving left pointer
        # max_profit = 0
        # left, right = 0, 1
        # while left < len(prices) - 1 and right < len(prices):
        #     diff = prices[right] - prices[left]
        #     if diff <= 0:
        #         left += right
        #         right += 1
        #     elif diff > 0:
        #         max_profit = max(diff, max_profit)
        #         right += 1
        # return max_profit
