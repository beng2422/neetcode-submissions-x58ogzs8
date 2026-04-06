class Solution:
    def findMin(self, nums: List[int]) -> int:

        while len(nums)>0:
            if len(nums)%2==0:
                half = len(nums)/2
            else:
                half = (len(nums)-1)/2
            #if nums is greater than 2
            if 2<len(nums):
                if nums[half]>nums[half+1]:
                    nums = nums[half:]
                else:
                    nums = nums[:half]


            elif nums[0]>nums[1]:
                return 1
            else:
                return 0

        