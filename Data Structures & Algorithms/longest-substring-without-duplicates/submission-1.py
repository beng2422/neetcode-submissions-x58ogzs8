class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window

        #I could have a set and start with two pointers at 0-n and if I can move left I will move left

        maxVal = 0
        val = set()
        #for i in range(len(s)):
        i = 0
        while i<len(s):
            r = i
            maxV = 0
            val = set()
            while r<len(s) and s[r] not in val:
                val.add(s[r])
                r+=1
                maxV +=1
            if maxV>maxVal:
                maxVal= maxV
            

            i = r


        return maxVal