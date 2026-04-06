class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        i = 0
        total = gas[0] - cost[0]
        currInd = 0
        while total<0:
            i += 1
            total = gas[i] - cost[i]
        
            currInd = i
        if i==0:
            i = 1
        print('firsti', i)
        print('firsttotal', total)
        movepast = False
        while i<len(gas) and total>=0:
            print('i', i , 'total', total)

            total = total +  (gas[i] - cost[i])
            print('i', i, 'gas', gas[i], 'cost', cost[i])

            
            if total<0:
                total = 0
                i+=1
                currInd = i
                movepast = False

            
            else:
                i+=1
                movepast = True
            if i>=len(gas):
                i = 0
          #  print('i', i)
                
           # print('total', total)
            if i == currInd and movepast:
                return currInd

        return 0