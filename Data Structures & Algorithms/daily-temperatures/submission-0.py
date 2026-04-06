class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]
        stack = []
        
        for i in range(len(temperatures)):
            j=i+1
            x = 0
            stack.append(0)
            if j<len(temperatures) and temperatures[j]>temperatures[i]:
                    res[i] = 1
                    continue
            else:
                y = False
                while j<len(temperatures) and temperatures[j]<=temperatures[i]:
                    stack[-1] += 1
                    y = True
                    

                    x+=1
                    if i == 1:
                        print(x)
                    j+=1
                x+=1
                if j == len(temperatures)-1:
                    x=0
                
            res[i] = 0 if j == len(temperatures) else j - i
           # res[i] = x
            stack = stack[:-1]
        print(stack)
        print(res)
        return res




        