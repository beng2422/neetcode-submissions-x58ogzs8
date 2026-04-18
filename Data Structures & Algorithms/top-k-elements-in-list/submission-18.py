from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = defaultdict(int)
        for i in nums:
            heap[i] += 1
        newH = []
        for i, val in heap.items():
            newH.append([-val, i])
        heapq.heapify(newH)
        ret = []
        for i in range(k) :
            ret.append(heapq.heappop(newH)[1])
        return ret

