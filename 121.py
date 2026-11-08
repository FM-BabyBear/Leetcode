class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0
        length = len(prices)

        for i in range(length):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit
