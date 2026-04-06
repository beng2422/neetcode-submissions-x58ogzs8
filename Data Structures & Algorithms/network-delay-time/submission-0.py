import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #classic use of dijkstras
        #remembering dijkstras: create a dict of all nodes, push them to the heap. pop the smallest val 
        #of the heap, look at all the neighbors and push the neighbors to the stack if they are smaller 
        #than they were before

        heap = [(float('inf'), i+1) for i in range(n)]
        heap[k-1] = (0, k)
        heapq.heapify(heap)
        distances = {i+1:float('inf') for i in range(n)}
        distances[k] = 0
        while heap:
            dist, node = heapq.heappop(heap)
            
            #iterate through all of the neighbs - see if we can update the dist, if we do push it to heap
        
            for edge in times:
                if edge[0]==node and distances[edge[1]]>dist+edge[2]:
                    distances[edge[1]] = dist+edge[2]
                    heapq.heappush(heap, (distances[edge[1]], edge[1]))



            
        print(distances)

        return max(distances.values()) if max(distances.values())!=float('inf') else -1



