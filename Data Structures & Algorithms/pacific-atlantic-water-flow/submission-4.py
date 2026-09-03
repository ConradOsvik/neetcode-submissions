class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def dfs(r, c, prev, ocean):
            if not 0 <= r < rows or not 0 <= c < cols:
                return

            if (r, c) in ocean:
                return

            if heights[r][c] < prev:
                return

            ocean.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)

        # Left/right edges
        for r in range(rows):
            dfs(r, 0, 0, pacific)
            dfs(r, cols - 1, 0, atlantic)

        # Top/bottom edges
        for c in range(cols):
            dfs(0, c, 0, pacific)
            dfs(rows - 1, c, 0, atlantic)

        return [[r, c] for r, c in pacific & atlantic]