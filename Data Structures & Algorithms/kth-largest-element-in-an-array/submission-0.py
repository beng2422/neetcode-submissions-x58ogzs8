class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsNeg = [-x for x in nums]
        heapq.heapify(numsNeg)
        for i in range(k):
            x = heapq.heappop(numsNeg)
        
        return -x