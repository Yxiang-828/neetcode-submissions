class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #must buy before sell
        #carry best future price with you
        n=len(prices)
        bestfuture=0
        maxo=0
        for i in range(n-1,-1,-1):
            bestfuture=max(bestfuture,prices[i])
            maxo=max(bestfuture-prices[i],maxo)
        return maxo
