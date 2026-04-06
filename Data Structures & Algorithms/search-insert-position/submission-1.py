class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l<=r:
            print(l, r)
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if mid==0 and nums[0]>target:
                return mid
            if mid==len(nums)-1 and nums[mid]<target:
                return mid+1
            elif 0<mid<len(nums)-1 and nums[mid] < target < nums[mid+1]:
                return mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid + 1
        print('failed')
        return -10