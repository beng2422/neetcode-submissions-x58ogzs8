class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            if i>=k-1:

              #  val, x =heapq.heappop(nums1)
                while heap[0][1]<=i-k:
                # heapq.heappush(nums1, [val, x])
                    val, x =heapq.heappop(heap)

                

                res.append(-heap[0][0])


        return res


        # maxI = 0
        # res = []

        # for i in range(len(nums)-k+1):
            
        #     res.append(max(set(nums[i:i+k])))



        # return res
