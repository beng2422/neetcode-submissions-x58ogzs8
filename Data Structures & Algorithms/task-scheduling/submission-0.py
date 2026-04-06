class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #Get dict of count of tasks - for each val -starting at largest count 
        #create a data structure that counts the number of steps left
        #keep going with the second one and subtract the 
        
        dict1 = {}
        for i in tasks:
            dict1[i] = dict1.get(i, 0) + 1
        array = [[-v, k] for k,v in dict1.items()]
        
        heapq.heapify(array)



        steps_left = []
        i = 0
        while array or steps_left:
            if array:
                task = heapq.heappop(array)
                val = task[1]
                count = -task[0]
                print(val, count)
                count -= 1
                if count>0:
                    steps_left.append([i, n, count])
            if not array:
                for j in range(len(steps_left)):
                    if j>=len(steps_left):
                        break
                    left_val = steps_left[j]
                    if left_val[2]<=0:
                        steps_left = steps_left[:j] + steps_left[j+1:]
                        j-=1

                    elif i - left_val[0]>left_val[1]:
                        new_cnt = left_val[2]-1
                        if new_cnt>0:
                            steps_left[j] = [i, left_val[1], new_cnt]
                        else:
                            steps_left = steps_left[:j] + steps_left[j+1:]
                            j-=1
                        break
            for j in range(len(steps_left)):
                   
                    if j>=len(steps_left):
                        break
                    left_val = steps_left[j]
                    print('left_val', left_val)
                    if left_val[2]<=0:
                        steps_left = steps_left[:j] + steps_left[j+1:]
                        j-=1



                
            print(steps_left)
           
            # if not steps_left:
            #     return i
            i+=1
        return i 


            

