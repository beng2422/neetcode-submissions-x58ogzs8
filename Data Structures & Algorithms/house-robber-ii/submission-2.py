class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        neg = [False for i in range(len(nums))]

        dp[0] = nums[0]
        neg[0] = True
        if len(nums)==1:
            return nums[0]
        dp[1] = nums[1]


        for i in range(2, len(nums)):
            maxVal2 = 0
            negVal = False
            for j in range(i-1):
                if dp[j]>maxVal2:
                    maxVal2=dp[j]
                    negVal = neg[j]

            #x = max(dp[:i-1])
            if len(nums)-1==i:
                maxVal = 0
                for j in range(len(dp)-2):
                    if not neg[j] and dp[j]>maxVal:
                        maxVal = dp[j]
                dp[i] = nums[i] + maxVal
                        
            else:
                neg[i] = negVal
                dp[i] = (maxVal2 + nums[i])
        print(neg)
        print(dp)
        return max(dp)
        