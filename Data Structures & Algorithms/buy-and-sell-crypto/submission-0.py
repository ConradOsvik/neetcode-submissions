class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        out = 0

        for i in range(len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = price
                continue

            profit = price - min_price
            if profit > out:
                out = profit
        
        return out

