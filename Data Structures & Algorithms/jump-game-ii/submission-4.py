class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = nums[0]
        if len(nums)==1:
            return 0

        res = 1
        farthest = nums[0]
        while r<len(nums)-1:
            print('farthest', farthest)
            print('r', r, 'l', l)
            for i in range(r-l):
                farthest = max(farthest, l+i + nums[l + i])
            l=r+1
            r += farthest
            res+=1
            if res>5:
                return res
        return res

            

