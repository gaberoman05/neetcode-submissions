class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l = 0
        prof = 0
        while r < len(prices):
            if prices[r] - prices[l] > prof:
                prof = prices[r] - prices[l]
            elif prices[r] < prices[l]:
                l = r
            r += 1
        return prof