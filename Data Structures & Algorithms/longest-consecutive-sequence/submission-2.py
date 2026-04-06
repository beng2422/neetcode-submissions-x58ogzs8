class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        done_set = set()
        for j in nums_set:
            if j - 1 in nums_set or j+1 in nums_set:
                done_set.add(j)
        if len(done_set)==0 and len(nums) != 0:
            return 1
        return len(done_set)



        