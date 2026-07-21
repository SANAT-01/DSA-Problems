class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land = 0
        shared = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land += 1
                    if r > 0 and grid[r - 1][c] == 1:
                        shared += 1
                    if c > 0 and grid[r][c - 1] == 1:
                        shared += 1
        
        return 4 * land - 2 * shared