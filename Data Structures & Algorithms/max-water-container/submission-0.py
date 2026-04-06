class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        left = 0
        right = len(heights)-1
        maxH = 0
        while left<right:
            h = min(heights[left], heights[right])*(right-left)
            if h>maxH:
                maxH = h
            
            else:
                if heights[left] > heights[right]:
                    right-=1
                else:
                    left+=1
        return maxH