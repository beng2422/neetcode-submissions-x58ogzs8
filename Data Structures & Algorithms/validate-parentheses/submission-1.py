class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        new_s = []
        if len(s)%2!=0:
            return False
        for i in range(len(s)//2):
            stack.append(s[i])
            new_s.append(s[len(s)-i-1])
        while len(stack)>0:
            val = stack.pop()
            val2 = new_s.pop()
            if val == '(' and val2 == ')' or val == ')' and val2 == '(' or val == '[' and val2 == ']' or val == ']' and val2 == '[' or val == '{' and val2 == '}' or val == '}' and val2 == '{':
                continue
            else:
                return False
        
        
        return True




        # right = s[len(s)//2:]
        # left = s[:len(s)//2]
        # if len(right)!=len(left):
        #     print('here')
        #     return False
        # if len(s)<2:
        #     return True
        

        # for i in range(len(right)):
        #     left_val = left[len(left)-i-1]
        #     if left_val == '(':
        #         left_val = ')'
        #     elif left_val == ')':
        #         left_val = '('
        #     elif left_val == '}':
        #         left_val = '{'
        #     elif left_val == '{':
        #         left_val = '}'
        #     elif left_val == '[':
        #         left_val = ']'
        #     elif left_val == ']':
        #         left_val = '['
        #     print()

        #     if left_val != right[i]:
        #         print('jere')
        #         return False

        # return True
            
        