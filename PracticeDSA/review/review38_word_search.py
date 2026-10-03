"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/backtrack/word_search.py until you're done.

Problem (Word Search, LeetCode 79):

Given an m x n grid of characters board and a string word, return
true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically
neighboring. The same cell may not be used more than once.

Example:
  board = [["A","B","C","E"],
           ["S","F","C","S"],
           ["A","D","E","E"]]
  word = "ABCCED" -> True
  word = "SEE"    -> True
  word = "ABCB"   -> False (the 'B' would need to be reused)

Write your solution below.
"""


def word_search(board, word):
    if not word:
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if word[0] == board[i][j]:
                found = dfs(board, word,i,j,0)
                if found:
                    return True

    return False

def dfs(board, word,r,c,i):

    if i >= len(word):
        return True

    if r < 0 or r>= len(board) or c < 0 or c>= len(board[0]) or board[r][c] == '#':
        return False

    char = board[r][c]

    if char == word[i]:
        board[r][c] = '#'
        i += 1

        found = (
            dfs(board, word,r+1,c,i) or
            dfs(board, word,r-1,c,i) or
            dfs(board, word,r,c-1,i) or
            dfs(board, word,r,c+1,i)

        )

        board[r][c] = char
        return found

    return False





if __name__ == "__main__":
    def make_board():
        return [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]

    fixed_cases = [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False),
        ("A", True),
        ("Z", False),
    ]
    for word, expected in fixed_cases:
        got = word_search(make_board(), word)
        assert got == expected, f"{word!r}: expected {expected}, got {got}"
    print("fixed cases passed")

    assert word_search([], "A") is False
    assert word_search([["A"]], "A") is True
    assert word_search([["A"]], "B") is False
    print("edge cases passed")

    import random
    import string

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
        got = word_search([row[:] for row in board], word)
        want = brute_force([row[:] for row in board], word)
        assert got == want, f"{board},{word!r}: expected {want}, got {got}"
    print("300 randomized trials passed")
