class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #. 1 add,   1-2 add.   121 add.   12stop.  1-1.   2
        #issue here is that if there are 2 of the same values, they will both be added
        #if its like 1,1,2 then it will treat each index as a unique val
        ret = []
        visited = set()
        cur = []
        nums = sorted(nums)
        print(nums)
        if len(nums)==0:
            return []
        def back(i):
            if tuple(cur) in visited:
                
                return
            if i>=len(nums) :
                ret.append(cur.copy())
                
                return

                
            cur.append(nums[i])

            back(i+1)
            visited.add(tuple(cur.copy()))
            cur.pop()
            #if nums[i]!=prev:
            back(i+1) 
            visited.add(tuple(cur.copy()))
        back(0)

       # ret.append([])
       # ret.append([nums[len(nums)-1]])
        return ret



