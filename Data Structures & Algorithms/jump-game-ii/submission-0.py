class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = nums[0]
        if len(nums)==1 and nums[0]>=0:
            return 1
        jumps = 0
        for i, val in enumerate(nums):
            if i == len(nums)-1 and furthest-1>=0:
                return jumps 
            if furthest-1>= val:

                furthest = furthest-1
            else:
                print('here')
                furthest = val
                jumps +=1
            print(furthest)
            # if furthest == 0:
            #     return False
        return jumps 

            