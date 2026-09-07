class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]
        for price in prices[1:]:
            if price < smallest:
                smallest = price
            if price - smallest > max_profit:
                max_profit = price - smallest
        return max_profit