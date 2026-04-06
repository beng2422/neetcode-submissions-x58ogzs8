class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp[i] = largest product
        #dp[i] = max(dp[i-1]*i, i)
        #min DP
        dp = [-10000000 for i in range(len(nums))]
        dpneg = [10000000 for i in range(len(nums))]
        dpneg[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
        
            
            dpneg[i] = min(dpneg[i - 1] * nums[i], dp[i - 1] * nums[i], nums[i])

        
        for i in range(1, len(nums)):
            x = dpneg[i-1]*nums[i] if dpneg[i-1] != 10000000 else 0
        
            
            dp[i] = max(dp[i-1]*nums[i], x, nums[i])

        maxVal = -10000000
        print(dp)
        for i in dp:
            maxVal = max(maxVal, i)
        return max(dp)










