class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/' and tokens[i] != '*':
                stack.append(int(tokens[i]))
            else:
                print(stack)
                res = 0
                val1 = stack[-1]
                stack = stack[:-1]
                val2 = stack[-1]
                stack = stack[:-1]
                print(val1, val2)
                print(tokens[i])
                if tokens[i] == '+':
                    res = val1+val2
                if tokens[i] == '-':
                    res = val2-val1
                if tokens[i] == '*':
                    res = val1*val2
                if tokens[i] == '/':
                    res = int(val2/val1)
                stack.append(res)
                
        return stack[0]