class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Running max profit
        # Seems more like two pointerish?
        # 
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        profit = 0
        while r < (len(prices)):
            if prices[l] < prices[r]:
                if prices[r] - prices[l] > profit:
                    profit = prices[r] - prices[l]
                r += 1
            else:
                l = r
                r = l + 1
        return profit
        