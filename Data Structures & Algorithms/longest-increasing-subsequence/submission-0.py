class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] = length of LIS including i
        #dp[i] = (length of dp[i-1] + 1 if its nums[i]> val of dp[i-1] greater else + 0, nums[i] if its greateer else dp[i-1])

        dp = [0 for _ in range(len(nums)+1)]
        for i in range(0, len(nums)):
            j = 0
            maxLength = 0
            while j<i:
                if nums[j]<nums[i] and maxLength<dp[j]:
                    maxLength = dp[j]
                j+=1
            dp[i] = maxLength+1
                
        print(dp)

        return max(dp)
            
                
            




        