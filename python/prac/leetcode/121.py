# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dbuy,dsell,max_profit = 0,None,0
        change = False
        for day in range(1,len(prices)):
            if prices[day] < prices[dbuy]:
                dbuy = day
            if all([day > dbuy, prices[day] > prices[dbuy]]):
                dsell = day
                change = True
            if change:
                profit = prices[dsell] - prices[dbuy]
                change = False
                if profit > max_profit:
                    max_profit = profit
        return max_profit
