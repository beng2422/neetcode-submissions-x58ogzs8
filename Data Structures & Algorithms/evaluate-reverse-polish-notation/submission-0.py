class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = int(tokens[0])
        val = None
        for i in range(1, len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/' and tokens[i] != '*':
                val = (int(tokens[i]))
            else:
                if tokens[i] == '+':
                    res += val
                if tokens[i] == '-':
                    res -= val
                if tokens[i] == '*':
                    res *= val
                if tokens[i] == '/':
                    res =int(res/val)
            print(res)
        return res