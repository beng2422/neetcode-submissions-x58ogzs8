import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                x = stack[-1]
                y = stack[-2]
                stack = stack[:len(stack)-2] + [x + y]
            elif i == '-':
                x = stack[-1]
                y = stack[-2]
                stack = stack[:len(stack)-2] + [y - x]
            elif i == '*':
                x = stack[-1]
                y = stack[-2]
                stack = stack[:len(stack)-2] + [x * y]
            elif i== '/':
                x = stack[-1]
                y = stack[-2]
                stack = stack[:len(stack)-2] + [int(y / x)]
            else:
                stack.append(int(i))
        print(stack)
        return int(stack[-1])
            