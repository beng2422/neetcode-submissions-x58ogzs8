class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in range(len(nums)):
            if val in dic.keys():
                
                return [dic[target-val], i]
            dic[target - val] = i
            
        