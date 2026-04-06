class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        while val in nums:
            nums.remove(val)
            k+=1
          #  print(x)
        return n-k
        
        for i in range(len(nums)):
            num = nums[i]
            if num == val:
                
                nums = nums[:i] + nums[i+1:]
                i-=1
            else:
                k+=1
            print(i, nums)
        return k
