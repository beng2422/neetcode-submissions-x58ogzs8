class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums[i] + nums[j] = -nums[k]
        #O(n^3) - for each pair check if there exists another value that is equal to -nums[i]-nums[j]
        #Idea: create an array of each pair -> takes O(n^2)
            #Then compare each value
        pairs = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    pairs[(i,j)] = nums[i] + nums[j]
        ret = []
        for i in range(len(nums)):
            for j in range(len(pairs.values())):
                if nums[i] == -pairs.values()[j]:
                    ret.append([i, pairs.keys()[j]])
        return ret


                
        

        
        