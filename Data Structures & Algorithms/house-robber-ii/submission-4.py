class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums)-1)]

        dp[0] = nums[0]
        if len(nums)==1:
            return nums[0]
        dp[1] = nums[1]

        dp1= [0 for i in range(len(nums))]

        if len(nums)==1:
            return nums[0]
        dp1[1] = nums[1]
        for i in range(2, len(nums)):
            x = max(dp1[:i-1])

          
            dp1[i] = (x + nums[i])
        for i in range(2, len(nums)-1):
            x = max(dp[:i-1])

          
            dp[i] = (x + nums[i])
         
        return max(dp+dp1)
        