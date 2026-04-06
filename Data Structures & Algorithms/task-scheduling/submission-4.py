import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #so we start with a max heap and once we use that value we remove it and put it in 
        #the queue. Once the heap 

        #

        count = {}
        for i in tasks:
            count[i] = count.get(i, 0) - 1
        counts = list(count.values())
        #print(counts)
        queue = []
        heapq.heapify(counts)
        print(counts)
        time = 0
        while queue or counts:
            print('t:', time, 'count', counts, 'queue', queue)

            if counts:
                left = heapq.heappop(counts)
                if left+1<0:
                    queue.append((left+1, time + n + 1))
            elif queue:
                if queue[0][1] <= time or queue[0][0]==0:


                   # heapq.heappush(counts, queue[0][0]+1)
                    x = (queue[0][0]+1, time+n+1)
                    queue = queue[1:] 
                    if x[0]<0:
                        
                        queue.append(x)
 
            #print()
            time += 1
        return time
        
            

        


