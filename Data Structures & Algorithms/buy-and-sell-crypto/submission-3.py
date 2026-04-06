class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find smallest value
        if len(prices)<=1:
            return 0
        maxProfit = prices[1] - prices[0]
        minVal = prices[0]
        for i in range(1, len(prices)):
            if prices[i]-minVal>maxProfit:
                maxProfit = prices[i]-minVal
            if prices[i]<minVal:
                minVal = prices[i]
        if maxProfit<0:
            maxProfit = 0
        return maxProfit


        