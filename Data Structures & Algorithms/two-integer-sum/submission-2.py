class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in dic.keys():
                
                return [dic[val], i]
            dic[target - val] = i
            
        