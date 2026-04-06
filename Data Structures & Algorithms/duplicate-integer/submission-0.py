class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create dictionary
        num_of_nums = {}
        for i in nums:
            if i in num_of_nums.keys():
                return True
            num_of_nums[i] = 1
        return False
         