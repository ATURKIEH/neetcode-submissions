class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        best_profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                if profit > best_profit:
                    best_profit = profit

        return best_profit

            
        


        