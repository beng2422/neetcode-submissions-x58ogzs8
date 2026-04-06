class Solution:
    def isValid(self, s: str) -> bool:
        right = s[len(s)//2:]
        left = s[:len(s)//2]
        if len(right)!=len(left):
            print('here')
            return False
        if len(s)<2:
            return True
        

        for i in range(len(right)):
            left_val = left[len(left)-i-1]
            if left_val == '(':
                left_val = ')'
            elif left_val == ')':
                left_val = '('
            elif left_val == '}':
                left_val = '{'
            elif left_val == '{':
                left_val = '}'
            elif left_val == '[':
                left_val = ']'
            elif left_val == ']':
                left_val = '['
            print()

            if left_val != right[i]:
                print('jere')
                return False

        return True
            
        