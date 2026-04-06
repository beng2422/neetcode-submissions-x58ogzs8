class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        val = [False, False, False]
        for i in triplets:
            if i[0] > target[0] or i[1]>target[1] or i[2] > target[2]:
                continue

            if i[0] == target[0]:
                val[0] = True
            if i[1] == target[1]:
                val[1] = True
            if i[2] == target[2]:
                val[2] = True
            if val[0] == True and val[1] == True and val[2] == True:
                return True
        
        return False




