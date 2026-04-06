class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp[i] = largest product
        #dp[i] = max(dp[i-1]*i, i)
        #min DP
        dp = [-10000000 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
        
            
            dp[i] = max(dp[i-1]*nums[i], nums[i])

        maxVal = -10000000
        print(dp)
        for i in dp:
            maxVal = max(maxVal, i)
        return maxVal










