class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)):
            j = i+1
            while j < len(prices):
                profit = prices[j] - prices[i]

                if profit >= best_profit:
                    best_profit = profit
                    j+=1

                else:
                    j+=1

        return best_profit


       


        