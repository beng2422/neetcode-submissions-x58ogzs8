class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][state] = profit of hold, sold, buy, rest (at state) from prices[:i] 
        #rest->hold = buy, dp[i][sell]=dp[i-1][rest]  
        #dp[i][buy] = dp[i-1][rest] - prices[i] 
        #dp[i][rest] = dp[i-1][buy] or dp[i-1][rest] -> those should be the same tho right
        #dp[i][hold] = dp[i-1][hold]

        

        #dp[i][hold] = max(dp[i-1]),  dp[i][sold] = prices[i] - dp[i-1][hold], 
        #dp[i][rest] = d
        dp = [[0,0,0,0] for i in range(len(prices))]
        #sell=1, hold=2, rest=3
        for i in range(len(prices)):
            if i>0:

               # dp[i][0] = dp[i-1][3] - prices[i]
                dp[i][1] = dp[i-1][2] + prices[i]
                dp[i][2] = max(dp[i-1][2], dp[i-1][3] - prices[i])
                dp[i][3] = max(dp[i-1][3], dp[i-1][1])
            else:
               # dp[i][0] = - prices[0]
                dp[i][1] = 0
                dp[i][2] = -prices[0]
                dp[i][3] = 0

        print(dp)
        return max(dp[len(prices)-1])
            
            



        