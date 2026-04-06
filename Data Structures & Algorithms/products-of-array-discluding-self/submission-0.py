import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 0

        for i in range(len(nums)):
            total = total*nums[i]
        
        ret = []
        
        for i in range(len(nums)):
            ret.append(total * math.exp(nums[i], -1) )
        return ret
        