class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        x = []


        done = 0
        for j in nums_set:
            in_set = False
            for setConsec in x:
                if j-1 in setConsec or j+1 in setConsec:
                    in_set = True
                    setConsec.add(j)
            if not in_set:
                y = set()
                y.add(j)
                x.append(y)
        longest_val = 0
        for j in x:
            if len(j)>longest_val:
                longest_val=len(j)

        return longest_val

                    



            






        #     if j - 1 in nums_set or j+1 in nums_set:
        #         done_set.add(j)

        # longest_cons = 0
        # lengths = {}
        # for j in done_set:
        #     if j-1 in done_set or j+1 in done_set:

        # if len(done_set)==0 and len(nums) != 0:
        #     return 1
        # return len(done_set)



        