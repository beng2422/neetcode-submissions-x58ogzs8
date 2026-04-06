import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesNeg = [-x for x in stones]
        heapq.heapify(stonesNeg)
        while len(stonesNeg)>1:
            x = heapq.heappop(stonesNeg)
            y = heapq.heappop(stonesNeg)

            if x<y:
                y = x-y
            
                heapq.heappush(stonesNeg, y)
        print(stonesNeg)
        return -stonesNeg[0] if len(stonesNeg)==1 else 0


        # y = y - x


        # z=-y
        # b=-x

        # z