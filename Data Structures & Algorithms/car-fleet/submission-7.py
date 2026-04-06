class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #initial thoughts to do it at each time step - that would be a waste tho
        #we sort position based on position, then calcluate the time when cars farther away catch up
        #we could do this by starting at each car's speed

        #we could do a variation of a stack- where we see how many time steps for each car (starting at fastest) it takes to reach the end
        #then we check the next val in stack - if it reaches then we remove it from the stack and update the shortest time 

        x = [(position[i], speed[i]) for i in range(len(position))]
        x = sorted(x)
        print(x)

        #time it came ()
        stack = [(target - i)/j for (i, j) in x ]
        print(stack)
        minvals = 0
        for i in range(len(stack)-2,-1,-1):
            if stack[i+1]<=stack[i]:
                stack[i+1]=stack[i]
        print(stack)

        y = set(stack)
        print(y)
        return len(y)



