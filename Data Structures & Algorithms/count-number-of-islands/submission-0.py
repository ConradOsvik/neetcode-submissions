class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.islands = 0
        
        def search(r, c) -> bool:
            if not 0 <= r < rows or not 0 <= c < cols:
                return False

            if grid[r][c] == "0" or grid[r][c] == "#":
                return False
            
            grid[r][c] = "#"
            
            search(r - 1, c)
            search(r, c - 1)
            search(r + 1, c)
            search(r, c + 1)
        
            return True

        for row in range(rows):
            for col in range(cols):
                if search(row, col):
                    self.islands += 1

        return self.islands