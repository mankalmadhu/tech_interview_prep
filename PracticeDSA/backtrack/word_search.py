"""
LeetCode Link: https://leetcode.com/problems/word-search/

Discussion & Logic:
- We use Depth First Search (DFS) to explore all possible paths starting from any cell that matches the first letter of the word.
- To achieve O(1) auxiliary space (excluding the recursion stack), we modify the board in-place. We mark visited cells with a special character (e.g., '#') to prevent revisiting them during the same DFS path.
- Once a DFS path completes (either finding the word or hitting a dead end), we backtrack by restoring the original character to the cell so it can be used by other potential paths.
- The base case for finding the word (i >= len(word)) must be checked BEFORE checking bounds to prevent returning False incorrectly if the final character is on the edge of the board.
- The loop in `exist()` checks all cells as potential starting points.

Complexity Analysis:
- Time Complexity: O(M * N * 3^L) where M is rows, N is columns, and L is the length of the word. We check every cell, and for each valid start, we branch in up to 3 directions (excluding the cell we came from) for up to L steps.
- Space Complexity: O(L) where L is the length of the word. This is the maximum depth of the call stack. Auxiliary space is O(1) due to in-place marking.
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not word:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    found = self.dfs(board, i, j, word, 0)
                    if found:
                        return True
        return False

    def dfs(self, grid, r, c, word, i):
        if i >= len(word):
            return True

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "#":
            return False

        backup = grid[r][c]
        if backup == word[i]:
            grid[r][c] = "#"
            i += 1

            char_found = (
                self.dfs(grid, r + 1, c, word, i)
                or self.dfs(grid, r - 1, c, word, i)
                or self.dfs(grid, r, c + 1, word, i)
                or self.dfs(grid, r, c - 1, word, i)
            )

            grid[r][c] = backup
            return char_found

        return False


if __name__ == "__main__":
    def make_board():
        return [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

    sol = Solution()
    fixed_cases = [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False),
        ("A", True),
        ("Z", False),
    ]
    for word, expected in fixed_cases:
        got = sol.exist(make_board(), word)
        assert got == expected, f"{word!r}: expected {expected}, got {got}"
    print("fixed cases passed")

    assert sol.exist([], "A") is False
    assert sol.exist([["A"]], "A") is True
    assert sol.exist([["A"]], "B") is False
    print("edge cases passed")

    import random

    def brute_force(board, word):
        rows, cols = len(board), len(board[0])

        def helper(r, c, i, visited):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            found = (
                helper(r + 1, c, i + 1, visited)
                or helper(r - 1, c, i + 1, visited)
                or helper(r, c - 1, i + 1, visited)
                or helper(r, c + 1, i + 1, visited)
            )
            visited.remove((r, c))
            return found

        for i in range(rows):
            for j in range(cols):
                if helper(i, j, 0, set()):
                    return True
        return False

    for _ in range(300):
        rows = random.randint(1, 4)
        cols = random.randint(1, 4)
        alphabet = "AB"
        board = [[random.choice(alphabet) for _ in range(cols)] for _ in range(rows)]
        word_len = random.randint(1, 4)
        word = "".join(random.choice(alphabet) for _ in range(word_len))
        got = sol.exist([row[:] for row in board], word)
        want = brute_force([row[:] for row in board], word)
        assert got == want, f"{board},{word!r}: expected {want}, got {got}"
    print("300 randomized trials passed")
