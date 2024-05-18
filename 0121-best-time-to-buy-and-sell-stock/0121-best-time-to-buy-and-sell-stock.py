class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        max_profit = 0
        while sell<len(prices):
            if prices[buy]>prices[sell]:
                buy=sell
                sell+=1
            else:
                max_profit=max(max_profit,prices[sell]-prices[buy])
                sell+=1
        return max_profit