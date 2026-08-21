class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = []
        
        for i, temp in reversed(list(enumerate(temperatures))):

            while len(stack) > 0 and temp >= stack[-1][1]:
                stack.pop()

            if len(stack) > 0:
                top = stack[-1]
                out.insert(0, top[0] - i)
            else:
                out.insert(0, 0)

            stack.append((i, temp))

        return out