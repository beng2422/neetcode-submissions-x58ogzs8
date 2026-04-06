class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #what we want to do is find distinct 4 sums. We can go about this by first finding all
        #pairs of 2sums, then try to combine them. We will keep track of each 2sum pair in 
        #a list of dicts keeping track of the sum and the indicees used to make sure its distinct
        twoSum = []
        indices = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                twoSum.append((nums[i]+nums[j], (i,j)))

        res = []
        resVals = []
        for i, (indSum1, (i1, j1)) in enumerate(twoSum):
           # print(indSum1, i1, j1)
            for j, (indSum2, (i2, j2)) in enumerate(twoSum):
                if i==j:
                    continue
                numVals = {}
                for num in [nums[i1], nums[i2], nums[j1], nums[j2]]:
                    numVals[num] = numVals.get(num, 0) + 1
                if numVals not in resVals and (indSum1 + indSum2)==target and i1!=i2 and i1!=j2 and j1!=j2 and j1!=i2:

                    resVals.append(numVals)
                    res.append([nums[i1], nums[i2], nums[j1], nums[j2]])



        
        return res



