class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #Basically we use the trick of counting all the sums and if 
        #sums[i] - sums[k] = k, then the difference exists  

        res = 0
        
        vals = [nums[0]]
        for i in range(1, len(nums)):
            vals.append(vals[i-1]+ nums[i])

        dict1 = {0: 1}
        for i in vals:
            if dict1.get(i-k) is not None:
                res+=dict1.get(i-k)

            dict1[i] = dict1.get(i, 0) + 1
        return res    
       


        # for i in range(len(nums)):

        #     curr = 0
        #     j = i
        #     print(i)
        #     while j < len(nums):
        #         curr += nums[j]
                
        #         if curr== k:
        #             print('here')
        #             res+=1
        #             break
        #         j+=1

        # return res