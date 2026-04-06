class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        #goal: to find where nums2 fits in nums1
        #run binary on both - at each step compare if curr1>curr2 - if thats true find the new mid for 
        #nums1 (it should be between curr1_ind and 0) and new curr2 should be between curr2_ind and len(nums2)
        #Base case if nums2[num2_ind-1]<=curr1<=curr2 or nums1[num1_ind-1]<=curr2<=curr1

        num1_ind = len(nums1)//2
        num2_ind = len(nums2)//2
        i = 0


        while 0<=num1_ind<len(nums1) and  0<=num2_ind<len(nums2):
            curr1 = nums1[num1_ind]
            curr2 = nums2[num2_ind]
            print('curr1', curr1)
            print('curr2', curr2)
            if (num2_ind - 1) >= 0 and nums2[num2_ind-1]<=curr1<=curr2:
                print('here1')
                if curr1==curr2:
                    return curr1
                
                if (len(nums2) + len(nums1))%2==0:
                    return (curr1+ nums2[num2_ind-1]) / 2
                else:
                    return curr2
            if (num1_ind - 1) >= 0 and nums1[num1_ind-1]<=curr2<=curr1:
                if curr1==curr2:
                    return curr1
                print('here2')
                if (len(nums2) + len(nums1))%2==0:
                    return (curr1+curr2-1) / 2
                else:
                    return curr2
            if not (num1_ind - 1) >= 0 and curr2<=curr1:
                if curr1==curr2:
                    return curr1
                if (len(nums2) + len(nums1))%2==0:
                    return (curr1+curr2-1) / 2
                else:
                    return curr1
            if not (num2_ind - 1) >= 0 and curr1<=curr2:
                if curr1==curr2:
                    return curr1
                if (len(nums2) + len(nums1))%2==0:
                    return (curr1+curr2-1) / 2
                else:
                    return curr1
            if nums1[num1_ind]>nums2[num2_ind]:
                num1_ind = (len(nums1)+num1_ind+1)/2
                num2_ind = (num2_ind)//2
            else:
                num2_ind = (len(nums2)+num2_ind+1)/2
                num1_ind = (num1_ind)//2
            


            i+=1
            if i>6:
                return 0.0
        
        if len(nums1)==0:
            if len(nums2)%2==0:
                return nums2[len(nums2)//2] - nums2[len(nums2)//2-1]
            return nums2[len(nums2)//2]
        if len(nums2)==0:
            if len(nums1)%2==0:
                return nums1[len(nums1)//2] - nums1[len(nums1)//2-1]
            return nums1[len(nums1)//2]
        if nums1[0]>nums2[0]:

            if len(nums1)>len(nums2):
                return float(nums1[len(nums1)-(len(nums1)+len(nums2))//2])
            elif len(nums1)==len(nums2):
                return (nums1[0] + nums2[len(nums2)-1])/2
            else:
                return float(nums2[len(nums1)-(len(nums1)+len(nums2))//2])
        else:
            if len(nums1)>len(nums2):
                return float(len(nums2)-nums1[(len(nums1)+len(nums2))//2])
            elif len(nums1)==len(nums2):
                return (nums2[0] + nums1[len(nums1)-1])/2
            else:
                return float(nums2[len(nums1)-(len(nums1)+len(nums2))//2])









        # while num1_ind<len(nums1):
        #     num1_ind = (len(nums1)+num1_ind+1)//2
        #     print(num1_ind)
        #     i+=1
        #     if i>4:
        #         return 0.0

        # print('done')
        # print(num2_ind)
        # while num2_ind>=0:
        #     num2_ind = (num2_ind)//2
        #     print(num2_ind)
        #     i+=1
        #     if i>4:
        #         return 0.0

        # return 0.0



