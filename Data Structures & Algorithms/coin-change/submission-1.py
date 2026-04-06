class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        #dp[i] = least number of coins needed for amount i 
        #dp[i] = min dp[i-coin] s.t.(dp[i-coin]!=-1 ) dp[0]=0
        #coin-i
        dp = [-1 for _ in range(amount+1)]
        dp[0]=0

        for i in range(1, amount+1):
            total = 0
            minTotal = 100000
            for k in range(len(coins)):
                coin = coins[k]
                if i==2:
                    print(dp[i-coin]<minTotal)
                    print(i, coin, k)

                if i-coin>=0 and i-coin<=amount and dp[i-coin] != -1 and dp[i-coin]<minTotal:
                    minTotal = dp[i-coin]+1
            if minTotal!=100000:
                dp[i] = minTotal
        print(dp)
        return dp[amount]
                
            


                
                    

                    



