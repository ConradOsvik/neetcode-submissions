class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.maxSize = 0

        def backtrack(r, c) -> int:
            if not 0 <= r < rows or not 0 <= c < cols:
                return 0

            cell = grid[r][c]
            if cell == 0 or cell == "#":
                return 0

            grid[r][c] = "#"

            return (
                1
                + backtrack(r - 1, c)
                + backtrack(r, c - 1)
                + backtrack(r + 1, c)
                + backtrack(r, c + 1)
            )

        for row in range(rows):
            for col in range(cols):
                self.maxSize = max(self.maxSize, backtrack(row, col))

        return self.maxSize
