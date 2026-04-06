class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i] = 
        #dp[i] = sum if 
        summedVals = sum(nums)
        if summedVals%2==1:
            return False

        half = summedVals/2



        # for i in range(half):


        def canPartitionRec(target, numsRec):
            if target == 0:
                return True
            if len(numsRec)==0:
                return False
            
            return canPartitionRec(target - numsRec[0], numsRec[1:]) or canPartitionRec(target, numsRec[1:])

        
        return canPartitionRec(half, nums)

        