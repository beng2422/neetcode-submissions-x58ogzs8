class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[nums[0]]
        for i in range(len(nums)):
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        return -1