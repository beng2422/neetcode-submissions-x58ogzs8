class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = int(tokens.pop(0))
        while tokens:
            val = int(tokens.pop(0))
            op = tokens.pop(0)
            if op == '*':
                curr *= val
            if op == '-':
                curr -= val
            if op == '/':
                curr = curr//val
            if op == '+':
                curr += val
        return curr
            
