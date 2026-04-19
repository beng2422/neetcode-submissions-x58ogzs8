
import heapq
import random
class MinStack:
# I think the way to do this is to keep it ordered always? But that would not be O(1)
# if minV = min(val, minV) -> if we pop - check if the val we popped is minV, if it is, we remove it and then we need to 
#
#push 4, -4, 2, 



    def __init__(self):
        self.stack = []
        self.minVals = []
        heapq.heapify(self.minVals)
        self.poppedHashes = []


    def push(self, val: int) -> None:
        rand =  random.random()
        self.stack.append([val, rand])
        heapq.heappush(self.minVals, [val, rand])
        
    
    def pop(self) -> None:
        self.poppedHashes.append(self.stack[-1][1])
        self.stack = self.stack[:len(self.stack)-1]


        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
      #  print(self.minVals)
       # print(self.stack)
        pop = heapq.heappop(self.minVals)
        while pop[1]  in self.poppedHashes:
            pop = heapq.heappop(self.minVals)
        heapq.heappush(self.minVals, pop)
        return pop[0]
        
