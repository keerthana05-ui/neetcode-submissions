class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        col = len(grid[0])
        islands = 0
        def sink(r,c):
            if r < 0 or r >= rows or c < 0 or c >= col or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            sink(r+1,c)
            sink(r,c+1)
            sink(r-1,c)
            sink(r,c-1)
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1":
                    islands += 1
                    sink(r,c)
        return islands       