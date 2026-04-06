class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'(':')', '{': '}', '[':']'}
        for i in range(len(s)):
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')', '}', ']']:
                if len(stack)>0 and dictionary[stack[0]]==i:
                    continue
                else:
                    return False
        return True 

