class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 1
        right = len(nums)

        while left<right:
            mid = (left+right)//2

            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[left]<nums[right-1]:
                right = mid
            else:
                left = mid-1
            

                
        return nums[0]
        