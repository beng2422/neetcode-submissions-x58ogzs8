class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window

        #I could have a set and start with two pointers at 0-n and if I can move left I will move left
        #The classic window way is to start at a node and move up or down depending if you can 
        #choices - do I start at a single val and slide? Or do I slide from the previous substring?


        #I vaguely remember - its something like once we have a substring we move on to the next val
        l = 0
        vSet = set()
        m = 0
        for i in range(len(s)):

            while l<=i and s[i] in vSet:
                vSet.remove(s[l])
                l+=1
            
            vSet.add(s[i])
            print(vSet)
            if len(vSet)>m:
                m=len(vSet)


        return m





        # maxVal = 0
        # val = set()
        # #for i in range(len(s)):
        # i = 0
        # while i<len(s):
        #     r = i
        #     maxV = 0
        #     val = set()
        #     while r<len(s) and s[r] not in val:
        #         val.add(s[r])
        #         r+=1
        #         maxV +=1
        #     if maxV>maxVal:
        #         maxVal= maxV
            

        #     i = r


        # return maxVal