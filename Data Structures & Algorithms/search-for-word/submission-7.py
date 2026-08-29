class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if not 0 <= r < rows or not 0 <= c < cols:
                return False

            char = board[r][c]
            if char != word[i]:
                return False
            
            board[r][c] = "#"

            found = (
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c - 1, i + 1) or
                backtrack(r + 1, c, i + 1) or
                backtrack(r, c + 1, i + 1)
            )

            board[r][c] = char

            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False