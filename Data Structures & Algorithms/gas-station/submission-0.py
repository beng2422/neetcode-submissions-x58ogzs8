class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        i = 0
        total = gas[i] - cost[i]
        currInd = 0
        while total<0:
            i += 1
            total = gas[i] - cost[i]
        
            currInd += 1
        while i<len(gas) and total>=0:
            total +=  gas[i] - cost[i]
            if total<0:
                total = 0
                i+=1
                currInd = i
            
            else:
                i+=1
            if i>=len(gas):
                i = 0
                
            print(total)
            if i == currInd:
                return currInd

