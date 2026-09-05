class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #must buy before sell
        pricee=deque(prices)
        n=len(prices)
        maxee=[]
        for i in range(n):
            maxee.append(max(pricee))
            pricee.popleft()
        maxo=0
        for i in range(n):
            maxo=max(maxo,maxee[i]-prices[i])
        return maxo
