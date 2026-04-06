class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #2 recursive calls: 1 to not add i, the other to add i




        ans = []

        def dfs(i, current, val):

            if target==val:
                ans.append(current.copy())
                return None
            if target<val or i>=len(nums):
                return 

            current.append(nums[i])
            dfs(i, current, val + nums[i])
            current.pop()
            dfs(i+1, current, val)


        dfs(0, [], 0)
        return ans