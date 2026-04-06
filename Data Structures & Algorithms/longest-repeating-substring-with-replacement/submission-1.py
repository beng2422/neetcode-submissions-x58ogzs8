class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        curr = {}

        ans = 0

        max_freq = 0
        left = 0
        for right in range(len(s)):
            curr[s[right]] = curr.get(s[right], 0)+1
            max_freq = max(  curr[s[right]] , max_freq)
            
            while right-left+1-max_freq>k:
                curr[s[left]] -= 1
                left+=1
            ans = max(ans, right-left+1)

        return ans


