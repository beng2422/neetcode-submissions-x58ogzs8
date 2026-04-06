class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = []
        maxVal = 0
        for i in range(len(nums)):
            if i >=len(nums):
                break
            num = nums[i]
           # print(nums)
            if num-1 not in nums:
                currVal = 1

                while num+1 in nums:
                    nums.remove(num)
                    num = num+1
                    i-=1
                    currVal+=1

                if currVal>maxVal:
                    maxVal = currVal
                # j = i
                # currVal = 1
                
                # while j<len(nums) and nums[j]-1 in nums:
                #     currVal+=1
                #     nums.remove(nums[j]-1)
                #     j+=1
                #     i-=1
                #     print(nums)
                    


            
        #print(vals)
        return maxVal


























        # nums_set = set(nums)
        # longest = 0
        # x = []


        # done = 0
        # for j in nums_set:
        #     in_set = False
        #     connects = []
        #     for setConsec in x:
        #         if j-1 in setConsec or j+1 in setConsec:
        #             in_set = True
        #             setConsec.add(j)
        #         if j 
        #     if not in_set:
        #         y = set()
        #         y.add(j)
        #         x.append(y)
        # longest_val = 0

        # j-1

        # hashset = set()
        # for i in nums:
        #     hashset.add(i)
            

        # for j in x:
        #     if len(j)>longest_val:
        #         print("J here", j)
        #         longest_val=len(j)

        # return longest_val

                    


        #above is O(n^2)
        #subproblem - whats the longest subseqquence of first i values
        #dp[i+1] = dp[i]
        #dp[0]=1

        #What if I used a hash set 
        #Sliding window approach
        #
            











        #     if j - 1 in nums_set or j+1 in nums_set:
        #         done_set.add(j)

        # longest_cons = 0
        # lengths = {}
        # for j in done_set:
        #     if j-1 in done_set or j+1 in done_set:

        # if len(done_set)==0 and len(nums) != 0:
        #     return 1
        # return len(done_set)



        