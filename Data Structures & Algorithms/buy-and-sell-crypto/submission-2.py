class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = prices[0], prices[0]
        profit = 0
        for i, v in enumerate(prices):
            if i != 0 and start > v:
                start = v
                end = v
            if end < v:
                end = v
                profit = max(profit, end - start)
        return profit


        