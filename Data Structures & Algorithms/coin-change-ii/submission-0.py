class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i][a]=# combinations that amount to a using coins[:i]

        #dp[0][0] = 0, dp[i][a] = sum (1+dp[i-1][k]) s.t. (coin + k = a)
        #dpia = dpi-1a + dp[i][a-coins[i-1]]
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1

#print(dp)
        for i in range(1, len(coins)+1):
            for a in range(amount+1):
               # summedVal = 0
                dp[i][a] = dp[i-1][a] 
                if a>=coins[i-1]:
                    dp[i][a]+= dp[i][a-coins[i-1]]
        print(dp)
        return dp[len(coins)][amount]