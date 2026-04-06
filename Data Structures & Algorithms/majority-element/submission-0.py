class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for key in count:
            if count[key]>len(nums)/2:
                return key
        return 0
        