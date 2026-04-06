class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #if 2 meet - smaller one explodess - if same size both explode (size is by magnitude)
        #do a stack like method - essentially 

        stack = []
        ret = []
        for i in asteroids:
            #if its negative and there is a positive val in the stack we handle collision
            if i<0 and len(stack)>0:
                pos = stack.pop()
                if pos>abs(i):
                    stack.append(pos)
                elif pos < abs(i):
                    ret.append(i)
            




            #if its negative and there is no values in the stack, just add it to ret
            if i<0 and not len(stack):
                ret.append(i)

            #if its positive just add it to the stack
            if i > 0:
                stack.append(i)
        ret = ret + stack

        return ret
