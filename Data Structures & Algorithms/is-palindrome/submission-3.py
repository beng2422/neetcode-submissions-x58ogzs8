class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            first = i
            last = len(s)-1-i
            print('i', i, 's[first]', s[first], 's[last]', s[last])
            if last<=last:
                break
            if s[first]!=s[last]:
                return False
        return True
        