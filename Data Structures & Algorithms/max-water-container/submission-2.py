class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #this is just two pointers right? 

        l, r = 0, len(heights) - 1
        ret = -float('inf')
        while l < r:
            ret = max(ret, min(heights[r],  heights[l]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return ret