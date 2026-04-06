class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #put them in a dictionary
#For each unique value we take the value with the max, 
#subtract one to the count, put it in the back, keep track of cooldown time - so then it will be ordered by cooldown time

        dic = {}
        for i in tasks:
            dic[i] = dic.get(i, 0) + 1
        queue = []
        for k, v in dic.items():

            queue.append((v, 0))
        curr_time = 0
        print(queue)
        while queue:
            num_left, time_started = queue.pop(0)
            curr_time+=1
            curr_cooldown = curr_time -( time_started + n) #did enough time pass?
            print(curr_cooldown)
            if curr_cooldown <= 0:
                curr_time += -curr_cooldown
            if num_left - 1>0:
                queue.append((num_left-1, curr_time))
            print(curr_time)
        return curr_time
            



