class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        if len(nums)==1:
            return 0

        res = 0
        farthest = 0
        while r<len(nums)-1:
            print('farthest', farthest)
            print('r', r, 'l', l)
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
              #  print('val', i, farthest, nums[l+i])
            l=r+1
            r = farthest
            res+=1
            if res>5:
                return res
        return res

            

