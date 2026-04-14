import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #we can use a heap here - the algo is pop all of the values 
        #with a valid enqueue time, then choose the value with the smallest processing time
        #hmm this might take a long time, what if all values are valid, then 
        #we would have to push them back and choose the smallest val
        #that approach would be O(n^2 ) still
        #another approach: take each 
        def getAvailableTasks(time, heap):
            i = 0
            ret = []
            while tasks and tasks[0][0] <= time:
                task = tasks.pop(0)
                heapq.heappush(heap, [task[1], task[2]])
            return heap
        tasks = [tasks[i] + [i] for i in range(len(tasks))]
        tasks.sort()
        print(tasks)
        heap = []
        heapq.heapify(heap)
        time = 0
        ret = []
        while tasks or heap:
            heap = getAvailableTasks(time, heap)
            if len(heap) == 0:
                time = tasks[0][0]
                continue
            task = heapq.heappop(heap)
            ret.append(task[1])
            time += task[0]
        return ret
            


            



