class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#so we could do it in O(n^2)
#what if we created a max variable- 
#30=max, 38-update it, 
#we need to keep track of all of the vals+indexes 
#what if we used maxheap? 
        
        res = [0]*len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            if len(stack)==0:
                stack.append((val, i))
            
                continue
            while stack and stack[-1][0]<val:
                _, j = stack.pop()
                res[j] = i-j
            
            stack.append((val, i))
        return res