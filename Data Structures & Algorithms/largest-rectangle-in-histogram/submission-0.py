class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #the assumption that I am making here is that we can while loop in both directions 
        #until we find a value larger than min and iterating through it will only be O(n)
        res = 0
      #  res=max(res, )
        for i in range(len(heights)):
            minVal = heights[i]

            currRes = heights[i]
            left, right = i-1,i+1
            while right < len(heights) and minVal<=(heights[right]):
                currRes += minVal
                right+=1
            while left >=0 and minVal<=(heights[left]):
                currRes += minVal
                left-=1
            print(currRes)
            res = max(res, currRes)
        return res
            

        