class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #basically for this question we can use binary search here
        #this means we try a random weight capacity and continusouly update it in a binary search way

        def greedyApproach(capacity):
            if capacity < max(weights):
                return 0, False
            i = 0 
            buckets = []
            while i < len(weights):
                if len(buckets) > 0 and buckets[-1] + weights[i] <= capacity:
                    buckets[-1] += weights[i]
                else:
                    buckets.append(weights[i])
                i += 1
            return len(buckets), True

        l, r = 0, sum(weights)
        while l <= r:
            capacity = (r + l + 1) // 2
            print(capacity, r, l)

            #use a greedy approach to see if it can fit within days days
            #need to check if anything less than this capacity fails
            numDays, val = greedyApproach(capacity)
            numDays2, val2 =  greedyApproach(capacity - 1)
            print('.  ', val, numDays, val2, numDays2)
            if not val:
                l = capacity + 1
                continue
            if numDays <= days < numDays2 or( numDays <= days and not val2):
                
                return capacity
            elif days < numDays: #need more days -> need to increase capacity 
                l = capacity + 1
            else: #
                r = capacity - 1
        print(l, r)
        return -1
                
            






            

        
