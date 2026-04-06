class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums[i] + nums[j] = -nums[k]
        #O(n^3) - for each pair check if there exists another value that is equal to -nums[i]-nums[j]
        #Idea: create an array of each pair -> takes O(n^2)
            #Then compare each value -> takes O(n^3)
        #MORE EFFECTIVE does it change if its sorted?
        #yes: subproblem: for each i consider how long 
        ret = []
        nums1 = sorted(nums)
        print(nums1)
        for i in range(len(nums1)-1):
            right = len(nums1) - 1
            left = i+1
            print(i)
            while right>left:
                total = nums1[i] + nums1[left]+nums1[right]
                if total==0:
                    ret.append([nums1[i],nums1[left],nums1[right]])
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        result = []
        lists=ret
        print('here', ret)
        
        for i in range(len(lists)):
            curr = sorted(lists[i])
            is_duplicate = False
            for j in range(i):
                if sorted(lists[j]) == curr:
                    is_duplicate = True
                    break
            if not is_duplicate:
                result.append(lists[i])
        
        return result
        return ret
                
        


        