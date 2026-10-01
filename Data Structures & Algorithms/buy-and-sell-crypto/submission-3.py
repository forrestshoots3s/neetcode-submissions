class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        for sell in prices:
           res = max(res, (sell - low))
           low = min(sell, low)
        return res