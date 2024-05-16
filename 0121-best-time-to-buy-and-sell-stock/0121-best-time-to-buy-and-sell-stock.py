class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profits.append(prices[r]-prices[l])
                r=r+1
            else:
                l=r
                r=r+1
        return max(profits)