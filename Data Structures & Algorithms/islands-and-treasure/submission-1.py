class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        INF = 2**31 - 1
        queue = deque()
        level = 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                (r, c) = queue.popleft()

                for nr, nc in [
                    (r - 1, c),
                    (r, c - 1),
                    (r + 1, c),
                    (r, c + 1)
                ]:
                    if (
                        0 <= nr < rows 
                        and 0 <= nc < cols
                        and grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = level
                        queue.append((nr, nc))

            level += 1