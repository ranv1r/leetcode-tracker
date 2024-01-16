class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                res = None
                if token == "+":
                    res = x + y
                elif token == "-":
                    res = x - y
                elif token == "*":
                    res = x * y
                elif token == "/":
                    res = x / y
                stack.append(int(res))
            else:
                stack.append(float(token))
        return int(stack.pop())