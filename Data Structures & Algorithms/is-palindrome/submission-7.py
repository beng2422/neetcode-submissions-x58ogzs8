class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for i in s:
            if str.lower(i) in 'abcdefghijklmnopqrstuvwxyz1234567890':
                newS = newS+str.lower(i)
        s= newS
        for i in range(len(s)):
            first = i
            last = len(s)-1-i
            print('i', i, 's[first]', s[first], 's[last]', s[last])
            if last<=first:
                break
            if s[first]!=s[last]:
                return False
        return True
        