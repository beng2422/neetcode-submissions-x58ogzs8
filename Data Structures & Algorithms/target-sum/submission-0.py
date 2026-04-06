class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #recurrence: dp[i][j] = current summed val 

       # dp = [0 for i in range(len(nums))]

        def recurse(nums, summedVal):
            if len(nums) == 0 and summedVal == target:
                return 1
            if len(nums) == 0:
                return 0
            
            return recurse(nums[1:], summedVal+nums[0]) + recurse(nums[1:], summedVal-nums[0])


        return recurse(nums, 0)
        