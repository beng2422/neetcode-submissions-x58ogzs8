class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Greedy approach - brute force it
        #dp base case: buy it (-prices[0]), at each point
        #take max of selling or staying


        # dp = [0]*len(prices)
        # dp[0] = -prices[0]
        # min_price
        profit = 0

        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i] - prices[i-1])
        return profit
            #dp[i] = max(dp[i-1], prices[i] - min_price)


        