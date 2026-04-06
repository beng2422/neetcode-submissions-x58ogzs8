class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        new_s = []
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            stack.append(s[i])
        
        right_vals = {')': '(',  '}': '{', ']': '['}
        i = 0
        

        while len(stack)>0 and i<len(stack):
            if i == 0:
                if i in right_vals.values():
                    return False
                else:
                    i+=1
                    continue
           

            if stack[i] in right_vals.keys():
                if right_vals[stack[i]]==stack[i-1]:
                    stack = stack[:i-1] + stack[i+1:]
                    i-=2
                else: 
                    return False
            i+=1
        if len(stack)==0:
            return True
        else:
            return False
        


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
            
        