class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = prices[0]
        for sell in prices:
           res = max(res, (sell-min))
           min = min(sell, min)
        return res