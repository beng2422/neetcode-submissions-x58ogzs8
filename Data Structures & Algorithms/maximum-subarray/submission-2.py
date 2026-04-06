class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #initially it looks like a dp type problem
        #we can set dp[i] = max subarray including that value 
        dp = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            if dp[i-1] + dp[i] > dp[i]:
                dp[i] = dp[i-1] + dp[i]
        return max(dp)

