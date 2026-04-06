class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #simple with dictionary
        #difficult in O(1) space
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        
        res = []
        for key, val in dict1.items():
            if val>len(nums)/3:
                res.append(key)
        return res
            

