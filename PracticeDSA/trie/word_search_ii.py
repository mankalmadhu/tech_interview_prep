# https://leetcode.com/problems/word-search-ii/
"""
Word Search II

Given an m x n grid of characters `board` and a list of strings
`words`, return all words from `words` that can be found in the
grid. Each word must be constructed from letters of sequentially
adjacent cells (horizontally or vertically neighboring, any
direction, can turn). The same cell may not be used more than once
per word.

Approach: insert every word into a trie, then backtrack from every
cell in the grid, extending the current path one neighbor at a time.
At each step, `trie.starts_with(path_so_far)` prunes any branch whose
accumulated path isn't a prefix of any word, and `trie.search` checks
whether the path so far is itself a complete word (appended once,
even if reached via multiple distinct paths). Recursion continues
past a found word (no early return) so that a word which is itself a
prefix of a longer word (e.g. "eta" / "etab") doesn't block the
longer match. `visited` is reset per starting cell and unmarked on
backtrack (mark/unmark), so a cell is only off-limits within the
current in-progress path, not across unrelated starting cells or
sibling branches.

Complexity Analysis:
--------------------
Time:  O(M * N * 4^L * L) - M*N starting cells, up to 4^L paths of
       length L from each (branching factor 4, depth bounded by L
       thanks to the `starts_with` prefix pruning), and each call
       does O(L) work building/looking up the accumulated string.
Space: O(W * L) for the trie (W words of avg length L, no shared
       prefixes) + O(L) for the recursion stack / `visited` / the
       strings built along a single path.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from trie import Trie  # noqa: E402


def solve(board, words):
    if not words:
        return []

    result = []
    trie = Trie()
    for word in words:
        trie.insert(word)

    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            visited = set()
            backtrack(trie, board, i, j, result, "", visited)

    return result


def backtrack(trie, board, r, c, result, cur_result, visited):
    if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or (r, c) in visited:
        return result

    next_result = cur_result + board[r][c]

    if not trie.starts_with(next_result):
        return result

    if next_result not in result and trie.search(next_result):
        result.append(next_result)

    visited.add((r, c))
    backtrack(trie, board, r + 1, c, result, next_result, visited)
    backtrack(trie, board, r, c + 1, result, next_result, visited)
    backtrack(trie, board, r - 1, c, result, next_result, visited)
    backtrack(trie, board, r, c - 1, result, next_result, visited)
    visited.remove((r, c))

    return result


if __name__ == "__main__":
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words1 = ["oei", "eta", "ieo", "vre"]
    assert sorted(solve(board1, words1)) == sorted(["oei", "eta", "ieo", "vre"])

    # prefix-of-another-word case: "eta" and "etab" both real paths
    board2 = [
        ["e", "t", "x"],
        ["z", "a", "b"],
        ["z", "z", "z"],
    ]
    words2 = ["eta", "etab", "nope"]
    assert sorted(solve(board2, words2)) == sorted(["eta", "etab"])

    # single cell, single-letter word
    board3 = [["a"]]
    words3 = ["a", "b"]
    assert sorted(solve(board3, words3)) == ["a"]

    # empty words list
    assert solve(board1, []) == []

    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(board, words):
        m = len(board)
        n = len(board[0])

        def dfs(r, c, idx, visited, word):
            if idx == len(word):
                return True
            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or (r, c) in visited
                or board[r][c] != word[idx]
            ):
                return False
            visited.add((r, c))
            found = (
                dfs(r + 1, c, idx + 1, visited, word)
                or dfs(r - 1, c, idx + 1, visited, word)
                or dfs(r, c + 1, idx + 1, visited, word)
                or dfs(r, c - 1, idx + 1, visited, word)
            )
            visited.remove((r, c))
            return found

        found_words = []
        for word in words:
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, 0, set(), word):
                        found_words.append(word)
                        break
                else:
                    continue
                break
        return found_words

    def random_board(rows, cols, alphabet="abc"):
        return [[random.choice(alphabet) for _ in range(cols)] for _ in range(rows)]

    def random_words(board, count, alphabet="abcd", max_len=4):
        m = len(board)
        n = len(board[0])
        words = []
        for _ in range(count):
            if random.random() < 0.5:
                length = random.randint(1, max_len)
                r, c = random.randrange(m), random.randrange(n)
                visited = {(r, c)}
                w = board[r][c]
                for _ in range(length - 1):
                    neighbors = [
                        (r + dr, c + dc)
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                        if 0 <= r + dr < m
                        and 0 <= c + dc < n
                        and (r + dr, c + dc) not in visited
                    ]
                    if not neighbors:
                        break
                    r, c = random.choice(neighbors)
                    visited.add((r, c))
                    w += board[r][c]
                words.append(w)
            else:
                length = random.randint(1, max_len)
                words.append("".join(random.choice(alphabet) for _ in range(length)))
        return words

    random.seed(42)
    trials = 300
    for t in range(trials):
        rows = random.randint(1, 4)
        cols = random.randint(1, 4)
        board = random_board(rows, cols, alphabet="abc")
        words = random_words(board, count=random.randint(1, 5), alphabet="abcd")

        expected = sorted(set(brute_force(board, words)))
        actual = sorted(set(solve(board, words)))

        assert expected == actual, (
            f"mismatch on trial {t}\nboard={board}\nwords={words}\n"
            f"expected={expected}\nactual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
