class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        path = []

        letters = [
            ["a", "b", "c"], 
            ["d", "e", "f"], 
            ["g", "h", "i"], 
            ["j", "k", "l"], 
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"]
        ]

        def backtrack(i):
            if i == len(digits):
                result.append("".join(path))
                return

            digit = int(digits[i])
            
            for j in range(len(letters[digit - 2])):
                char = letters[digit - 2][j]
                path.append(char)
                backtrack(i + 1)
                path.pop()

        backtrack(0)

        return result