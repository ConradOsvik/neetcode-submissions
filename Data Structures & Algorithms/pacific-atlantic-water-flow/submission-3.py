class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        solution = []
        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def pacific_dfs(r, c, prev):
            if not 0 <= r < rows or not 0 <= c < cols:
                return

            if (r, c) in pacific:
                return

            if heights[r][c] < prev:
                return
            
            pacific.add((r, c))

            for dr, dc in directions:
                pacific_dfs(r + dr, c + dc, heights[r][c])

            return

        def atlantic_dfs(r, c, prev):
            if not 0 <= r < rows or not 0 <= c < cols:
                return

            if (r, c) in atlantic:
                return

            if heights[r][c] < prev:
                return
                    
            atlantic.add((r, c))

            for dr, dc in directions:
                atlantic_dfs(r + dr, c + dc, heights[r][c])

            return
            
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_dfs(r, c, 0)
                if r == rows - 1 or c == cols - 1:
                    atlantic_dfs(r, c, 0)

        print(pacific)
        print(atlantic)

        common = pacific & atlantic

        print(common)

        for (r, c) in common:
            solution.append([r, c])

        return solution