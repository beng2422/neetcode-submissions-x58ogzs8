class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #the assumption that I am making here is that we can while loop in both directions 
        #until we find a value larger than min and iterating through it will only be O(n)
        res = 0
        stack = []
        left = [-1]*len(heights) #holds the left_index of the heights value closest to i, where heights[i]>heights[left]

        for i in range(1, len(heights)):
            j=i-1

            while j>=0 and heights[j]>=heights[i]:
                j = left[j]

            left[i] = j
        print(left)
        

        right = [len(heights)]*len(heights) #holds the left_index of the heights value closest to i, where heights[i]>heights[left]

        for i in range(len(heights)-2, -1, -1):
            j=i+1

            while j>=0 and j<len(heights) and heights[j]>=heights[i]:
                j = right[j]

            right[i] = j
        print(right)
        
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (right[i]-left[i]-1))

        return res



        # mapping = {}
        # for i in range(len(heights)):
        #     mapping[i] = (index_of_heights(min(heights[:i] + [heights[i]])), index_of_heights(min(heights[i:] + [heights[i]])))
            


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
            

        