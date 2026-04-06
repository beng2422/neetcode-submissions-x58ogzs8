class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #we could do some dp solution
        #seems like we could also use a sliding window approach

        i = 0
        l = 0
        currSum = 0
        ret = float('inf')
        while i < len(nums):

            while currSum - nums[l] >= target:
                currSum -= nums[l]
                l += 1
            
            if currSum < target:
                currSum += nums[i]
            
            if currSum >= target:
                ret = min(ret, i - l)
            i += 1
        
        return 0 if ret == float('inf') else ret


        
