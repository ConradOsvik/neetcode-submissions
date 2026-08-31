class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxSize = 0

        def backtrack(r, c) -> int:
            if not 0 <= r < rows or not 0 <= c < cols:
                return 0

            cell = grid[r][c]
            if cell == 0:
                return 0

            grid[r][c] = 0

            return (
                1
                + backtrack(r - 1, c)
                + backtrack(r, c - 1)
                + backtrack(r + 1, c)
                + backtrack(r, c + 1)
            )

        for row in range(rows):
            for col in range(cols):
                maxSize = max(maxSize, backtrack(row, col))

        return maxSize
