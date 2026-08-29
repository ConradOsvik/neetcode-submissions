class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.found = False
        
        def backtrack(r, c, path, key = None):
            if "".join(path) == word:
                self.found = True
                return

            if len(word) > rows*cols:
                return

            if not 0 <= r < rows:
                return
            if not 0 <= c < cols:
                return

            if board[r][c] != word[len(path)]:
                return

            path.append(board[r][c])

            relations = {
                "left": "right",
                "up": "down",
                "right": "left",
                "down": "up"
            }

            moves = {
                "left": (r - 1, c),
                "up": (r, c - 1),
                "right": (r + 1, c),
                "down": (r, c + 1)
            }

            for k, (x, y) in moves.items():
                if key in relations and relations[key] == k:
                    continue

                backtrack(x, y, path, k)

            path.pop()

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, [])

        return self.found