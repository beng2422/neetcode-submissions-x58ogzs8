class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[-1,0,2,4,6,8] -> mid = 2, 

        l, r = 0, len(nums)-1
        while l<=r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1
