class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        flows = []

        def bfs(r, c):
            queue = deque([(r, c)])
            visited = {(r, c)}

            pacific = False
            atlantic = False

            directions = [
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1)
            ]

            while queue:
                r, c = queue.popleft()

                if r == 0 or c == 0:
                    pacific = True

                if r == rows - 1 or c == cols - 1:
                    atlantic = True

                if pacific and atlantic:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not 0 <= nr < rows or not 0 <= nc < cols:
                        continue

                    if (nr, nc) in visited:
                        continue

                    if heights[nr][nc] > heights[r][c]:
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

            return False

        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    flows.append([r, c])

        return flows