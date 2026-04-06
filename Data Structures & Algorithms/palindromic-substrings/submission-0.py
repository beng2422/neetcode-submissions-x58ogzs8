class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 1
        if len(s)==1:
            return 1
        longest = ''
        for i in range(len(s)-1):
            curr = s[i]
            left = i-1
            right = i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                curr = s[left] + curr + s[right]
                right+=1
                left-=1
                count+=1
            print(curr)
            if len(curr)>len(longest):
                longest = curr
            left = i
            right = i+1
            curr = ''
            print(i, 'left', left, 'right', right, s[left], s[right])
            while left>=0 and right<len(s) and s[left] == s[right]:
                curr = s[left] + curr + s[right]
                right+=1
                left-=1
                count+=1
            print(curr)
            if len(curr)>len(longest):
                longest = curr
            count+=1
        return count

            
        