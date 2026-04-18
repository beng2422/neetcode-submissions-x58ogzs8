class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        i = 0
        lookup = {')': '(', '}': '{',  ']': '[' }
        while i < len(s):
            print('x here', i, x)
            if s[i] in [')', '}', ']'] and len(x) and x[-1] != lookup[s[i]]:

                    return False
            elif s[i] in [')', '}', ']'] and not len(x):
                return False
            elif s[i] in [')', '}', ']'] and len(x) and x[-1] == lookup[s[i]]:
                x.pop()
            elif s[i] in ['(',  '{',  '[']:
                x.append(s[i])

            i += 1
        
        return 0 == len(x)


