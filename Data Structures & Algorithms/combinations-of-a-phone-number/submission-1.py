class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []

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

        def backtrack(i, path):
            if i == len(digits):
                result.append(path)
                return

            digit = int(digits[i])
            
            for j in range(len(letters[digit - 2])):
                path += letters[digit - 2][j]
                backtrack(i + 1, path)
                path = path[:-1]

        backtrack(0, "")

        return result