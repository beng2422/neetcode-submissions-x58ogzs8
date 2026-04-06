class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2

            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[left]<nums[right-1]:
                right = mid+1
            else:
                left = mid
            

                
        return nums[left]
        