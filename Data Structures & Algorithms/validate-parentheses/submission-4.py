class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []

        for bracket in s:
            if bracket in pairs.keys():
                if stack:
                    top = stack.pop()
                    if top != pairs[bracket]:
                        return False
                else:
                    return False

            else:
                stack.append(bracket)
        
        if stack:
            return False

        return True