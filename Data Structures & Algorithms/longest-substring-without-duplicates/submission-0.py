class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longestSub = 0
        curr = set()
        left = 0
        for i in range(len(s)):

            
            while left<i:
                if s[i] in curr:
                    
                    curr.remove(s[left])
                    left+=1
                else:
                    break
            curr.add(s[i])
            longestSub = max(longestSub, i - left + 1)
        return longestSub