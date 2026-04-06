class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #when choosing between going left or right: 
        #go left when rightmost val - mid val < target


        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (right+left )// 2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]: #left half is sorted

                if nums[left]<=target and target<nums[mid]:#nums is on left hand side
                    right = mid-1
                else:
                    left = mid+1

            else:

                if target<=nums[right] and target>nums[mid]:#nums is on left hand side
                    left = mid+1
                else:
                    right = mid-1

        return -1
