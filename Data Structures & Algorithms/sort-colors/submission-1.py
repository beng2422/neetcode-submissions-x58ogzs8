class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        vals = {0: 0, 1:0, 2:0}

        for i in nums:
            vals[i] += 1
        here = False
        while True:
            here = False

            for i in range(1, len(nums)):
              #  print(nums[i-1], nums[i])
                if nums[i-1] > nums[i]:
                    temp = nums[i-1]
                    nums[i-1] = nums[i]
                    nums[i] = temp
                    here = True
                    break
            if here == False:
                return nums
        return nums
                 


        