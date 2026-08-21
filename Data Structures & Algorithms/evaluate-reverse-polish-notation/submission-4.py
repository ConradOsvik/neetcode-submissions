class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
            "/": lambda x, y: math.trunc(y / x)
        }

        stack = []

        for token in tokens:
            if token in operations:
                x = stack.pop()
                y = stack.pop()
                val = operations[token](x, y)
                stack.append(val)
            else:
                stack.append(int(token))

        return stack.pop()