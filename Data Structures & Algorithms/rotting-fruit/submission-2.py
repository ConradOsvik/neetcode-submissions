# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         maxTime = 0

#         def bfs(r, c) -> int:
#             if grid[r][c] != 2:
#                 return 0

#             queue = deque([(r, c)])
#             count = -1

#             while queue:
#                 l = len(queue)

#                 print("1", queue)

#                 for i in range(l):
#                     (r, c) = queue.popleft()

#                     if not 0 <= r < rows or not 0 <= c < cols:
#                         continue

#                     if grid[r][c] != 1 and grid[r][c] != 2:
#                         continue

#                     for nr, nc in [
#                         (r - 1, c),
#                         (r, c - 1),
#                         (r + 1, c),
#                         (r, c + 1)
#                     ]:
#                         if (
#                             0 <= nr < rows
#                             and 0 <= nc < cols
#                             and grid[nr][nc] == 1
#                         ):
#                             grid[nr][nc] = 2
#                             queue.append((nr, nc))

#                     grid[r][c] = -1

#                 print("2", queue)
                    
#                 count += 1

#             return count

#         for r in range(rows):
#             for c in range(cols):
#                 maxTime = max(maxTime, bfs(r, c))

#         print(grid)

#         return maxTime

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = -1
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue:
            l = len(queue)

            for i in range(l):
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
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes if minutes != -1 else 0
