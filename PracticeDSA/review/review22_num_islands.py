"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/num_islands.py until you're done.

Problem (Number of Islands, LeetCode 200):

Given an m x n 2D binary grid (grid[r][c] is "1" for land, "0" for
water), return the number of islands. An island is formed by
connecting adjacent lands horizontally or vertically (no diagonals),
and is surrounded by water.

Example:
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"],
  ]  -> 1

  grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
  ]  -> 3

Write your solution below (DFS or BFS flood-fill).
"""


class Solution:
    def numIslands(self, grid):
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self._dfs(grid,i,j)
                    num_islands += 1

        return num_islands


    def _dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c>= len(grid[0]) or grid[r][c] != "1":
            return

        grid[r][c] = "#"

        self._dfs(grid ,r+1, c)
        self._dfs(grid ,r-1, c)
        self._dfs(grid ,r, c+1)
        self._dfs(grid ,r, c-1)


if __name__ == "__main__":
    import copy

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().numIslands(copy.deepcopy(grid1)) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().numIslands(copy.deepcopy(grid2)) == 3

    grid3 = [["0"]]
    assert Solution().numIslands(copy.deepcopy(grid3)) == 0

    grid4 = [["1"]]
    assert Solution().numIslands(copy.deepcopy(grid4)) == 1

    print("fixed cases passed")
