class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        furthest = nums[0]
        if len(nums)==0 and nums[0]>=0:
            return True
        for i, val in enumerate(nums):
            if i == len(nums)-1 and furthest-1>=0:
                return True
            furthest = max(furthest-1, val)
            print(furthest)
            if furthest == 0:
                return False
        return True

            