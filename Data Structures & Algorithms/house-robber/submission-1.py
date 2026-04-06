class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = max amount u can rob including i 
        #dp[i] = nums[i] + dp[i-2]

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        if len(nums)==1:
            return nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = (dp[i-2] + nums[i])

        return max(dp)
        