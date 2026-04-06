class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums1 = set()
        for i in nums:
            if i in nums1:
                return i
            nums1.add(i)

        return -1