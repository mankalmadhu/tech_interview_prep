from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Finds the total number of distinct islands in a 2D binary grid.
        Time Complexity: O(M * N) | Space Complexity: O(M * N) (worst-case recursion stack)
        
        The Logic:
        - Treat the grid as an implicit graph where neighbors are up/down/left/right.
        - Iterate through every cell. When you find a '1' (land), you've found an island.
        - Trigger a Depth First Search (DFS) from that cell to find all connected land.
        - CRITICAL: To avoid double-counting or infinite loops, "sink" the island
          by converting visited '1's into '#'s (or '0's) directly in the grid.
          This achieves O(1) auxiliary space beyond the recursion stack!
        """
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1
        
        return islands

    def dfs(self, grid, r, c):

        if ( r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1'):
            return

        grid[r][c] = '#'
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

if __name__ == '__main__':
    sol = Solution()
    
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Test 1 -> Expected: 1, Got:", sol.numIslands(grid1))
    
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Test 2 -> Expected: 3, Got:", sol.numIslands(grid2))
    
    print("All tests executed!")
