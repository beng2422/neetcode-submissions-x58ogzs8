class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #COMPUTE ARRIVAL TIME = (target - position) / speed
        #If arrival time of a sorted positioni < positioni-1 then change arrival time of i-1=arrival time of i - 1
        #after you havev arrival times, find the 'holes'

        arrivalTimes = [int((target - position[i]) / speed[i]) for i in range(len(position))]
        print(arrivalTimes)
        cars = list(zip(position, arrivalTimes))
        cars.sort()
        for i in range(len(cars)):
            pos, a = cars[i]
            arrivalTimes[i] = a
            position[i] = pos
        print(arrivalTimes)
        for i in range(len(position)-1, -1, -1):
            print('here', i, i+1)
            if i+1<len(position) and arrivalTimes[i+1]>=arrivalTimes[i]:
                arrivalTimes[i] = arrivalTimes[i+1]-1
        numHoles = 0
        for i in range(len(arrivalTimes)-1):
            if 1+arrivalTimes[i]!=arrivalTimes[i+1]:
                numHoles+=1
        print(arrivalTimes)
        return numHoles+1






        #start from end of positions - add 
        # finished = [1 for _ in range(len(position))]
        # while sum(finished)!=0:
        #     for i in range(len(position)-1, 0, -1):
        #         newPos = position[i] + speed[i]
        #         if i+1<len(position) and newPos<position[i+1] and position[i]<target:
        #             position[i] = newPos
        #         elif i+1<len(position) and position[i]<target:
        #             position[i] = position[i+1]-1
        #         else:
        #             position[i] = newPos
            
        #         if position[i]>=target:
        #             finished[i] = 0
        # print(finished)
        # return []




