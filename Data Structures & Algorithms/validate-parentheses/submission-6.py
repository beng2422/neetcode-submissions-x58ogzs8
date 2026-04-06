class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'(':')', '{': '}', '[':']'}
        rest = ''
        for i in range(len(s)):
            print(i)
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif s[i] in [')', '}', ']']:
                rest = s[i:]
                break
        print('stack', stack)

        while stack: 
                x = stack.pop()
                y = rest[0]
                rest = rest[1:]
                print(x, y)

                if dictionary[x]==y:
                    continue
                else:
                    return False
        if len(stack)>0:
            return False
        return True 

