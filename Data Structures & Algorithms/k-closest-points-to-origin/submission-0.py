import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        lengths = [math.sqrt(x[0]**2 + x[1]**2) for x in points]
        dict1 = {}
        for i in range(len(lengths)):
            dict1[lengths[i]] = dict1.get(lengths[i], [])+[points[i]]
        print(lengths)
        heapq.heapify(lengths)
        newList = []
        for i in range(k):
            x = heapq.heappop(lengths)
            newList.append(dict1[x].pop())
            if not dict1[x]:
                del dict1[x]



        print(newList)
        return newList