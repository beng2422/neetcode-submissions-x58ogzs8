class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        #decision tree: 1 -> 2 -> 3
                        #   -> 3 -> 2
                        # 2 -> 1 -> 3
                        # 3 -> 1 -> 2

                        



        def backtrack(path, used):

            if len(path)==len(nums):
                ret.append(path.copy()) 
            


            for x in range(len(nums)):
                if nums[x] not in used:

                    path.append(nums[x])
                    used.append(nums[x])
                
                    backtrack(path, used)
                    path.pop()
                    used.pop()
        backtrack([], [])
        return ret
