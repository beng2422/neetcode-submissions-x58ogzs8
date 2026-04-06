class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #we could do some dp solution
        #seems like we could also use a sliding window approach

        i = 0
        l = 0
        currSum = 0
        ret = float('inf')
        while i < len(nums):
            currSum += nums[i]

            while currSum - nums[l] >= target:
                currSum -= nums[l]
                l += 1
           # print(i, l)

            
            if currSum >= target:
                ret = min(ret, i - l + 1)
            i += 1
          #  print(currSum)
        
        return 0 if ret == float('inf') else ret


        
