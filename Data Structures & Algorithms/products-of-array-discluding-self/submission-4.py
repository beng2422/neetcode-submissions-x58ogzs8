
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        num_zeros = 0

        for i in range(len(nums)):
            if nums[i]==0 and (num_zeros == 0 or num_zeros == 1):
                print('jere', nums[i])
                num_zeros+=1
            elif nums[i]==0:
                total = 0
            else:
                total = total*nums[i]
        
        ret = []
        print("total", total, num_zeros)
        
        for i in range(len(nums)):
            if nums[i]==0 and num_zeros == 1:
                
                ret.append(int(total))
            elif nums[i]!=0 and num_zeros == 1:
                ret.append(0)
            elif num_zeros == 2:
                ret.append(0)
            else:
                  ret.append(int(total*pow(nums[i], -1)))
        return ret
        