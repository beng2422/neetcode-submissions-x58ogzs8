class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #if 2 meet - smaller one explodess - if same size both explode (size is by magnitude)
        #do a stack like method - essentially 

        stack = []
        ret = []
        i = 0
        while i < len(asteroids):

            val = asteroids[i]
            # print(stack)
        
            #if its negative and there is a positive val in the stack we handle collision
            if val<0 and len(stack)>0 and stack[-1] > 0:
                #print('inside', stack, val)

     
                while len(stack) and stack[-1] > 0 and stack[-1]<abs(val):
                    stack.pop()
                if len(stack) and  stack[-1] > 0 and stack[-1] == abs(val):
                    stack.pop()
                elif len(stack) == 0 or stack[-1]<0:
                    stack.append(val)

            #if its negative and there is no values in the stack, just add it to ret
            elif val<0 and (not len(stack) or stack[-1] < 0):
                stack.append(val)

            #if its positive just add it to the stack
            elif val > 0:
                stack.append(val)
            i+=1
       
        # print('stack here', stack)
        return stack