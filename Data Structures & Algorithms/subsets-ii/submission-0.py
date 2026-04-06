class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #. 1 add,   1-2 add.   121 add.   12stop.  1-1.   2
        ret = []
        cur = []
        nums = sorted(nums)
        print(nums)
        if len(nums)==0:
            return []
        def back(i, prev):

            if i>=len(nums):
                ret.append(cur.copy())
                return

                
            cur.append(nums[i])

            back(i+1, nums[i])
            cur.pop()
            if nums[i]!=prev:
                back(i+1, nums[i]) 
        back(0, -10000)

        ret.append([])
        #ret.append([nums[len(nums)-1]])
        return ret



