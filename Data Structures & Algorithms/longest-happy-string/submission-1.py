
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #greedy approach - add the largest val of a b and c 
        heap = []
        if a:
            heap.append((-a, 'a'))
        if b:
            heap.append((-b, 'b'))
        if c:
            heap.append((-c, 'c'))
        #heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        
        heapq.heapify(heap)
        ret = ''
        i = 0
        while heap:
            i += 1
           # if i == 10:
               # return ''
            print(heap)
                #so what im thinking about is how do I get the largest 
                        #key,val pair from maxV quickly? 
            val = heapq.heappop(heap)

            if len(ret) >= 2 and val[1] == ret[-1] and val[1] == ret[-2]:
                if not heap:
                    return ret
                print("HEREEE", val)
                val1 = heapq.heappop(heap)
                heapq.heappush(heap, val)
                val = val1
                print("HEREEE", val)

            ret += (val[1])
            if val[0] != -1:
                
                heapq.heappush(heap, (val[0]+1, val[1]))
        return ret
