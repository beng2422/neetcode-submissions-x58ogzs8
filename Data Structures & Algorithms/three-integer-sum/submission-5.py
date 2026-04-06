class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums[i] + nums[j] = -nums[k]
        #O(n^3) - for each pair check if there exists another value that is equal to -nums[i]-nums[j]
        #Idea: create an array of each pair -> takes O(n^2)
            #Then compare each value
        keys = []
        values = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    keys.append((i,j))
                    
                    values.append(nums[i] + nums[j])
        ret = set()
        for i in range(len(nums)):
            for j in range(len(values)):
                if nums[i] == -values[j] :
                    a, b = keys[j]
                    ret.add([sorted([nums[i], nums[a], nums[b]])])
        return ret


                
        


        