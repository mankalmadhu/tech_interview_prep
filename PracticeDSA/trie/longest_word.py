# https://leetcode.com/problems/longest-word-in-dictionary/
"""
Longest Word in Dictionary

Given an array of strings `words`, find the longest word that can be
built one character at a time by other words in `words` (i.e. every
prefix of the word, built up one char at a time, must itself be a
complete word present in `words`). If multiple words of the max
length qualify, return the lexicographically smallest. If none
qualify, return "".

Two approaches are implemented:

1. `solve` - sort words by (-length, word) so the longest/lex-smallest
   candidates come first, then for each candidate walk its prefixes
   through the trie checking `is_end` at every step. Returns the
   first candidate whose full prefix-chain is valid.

2. `solve_dfs` - skips sorting entirely. Walks the trie itself
   starting at the root, only descending into a child when that
   child's `is_end` is True (which guarantees, by construction, that
   every node reached this way has a fully valid prefix-chain already
   confirmed on the way down). Tracks the best (longest, then
   lexicographically smallest) word seen during the walk.

Complexity Analysis:
--------------------
`solve`:
  Time:  O(N log N * L + N * L) - sorting N words of avg length L,
         then O(L) prefix-walk per candidate in the worst case.
  Space: O(N * L) for the trie.

`solve_dfs`:
  Time:  O(N * L) - every trie node is visited at most once.
  Space: O(N * L) for the trie + O(L) recursion depth.
"""

from trie import Trie


def solve(words):
    if not words:
        return ""

    trie = Trie()
    for word in words:
        trie.insert(word)

    words_sorted = sorted(words, key=lambda w: (-len(w), w))

    for word in words_sorted:
        i = len(word) - 1
        cur = word
        while i >= 0:
            if i == 0:
                return word

            if trie.search(cur[:i]):
                i -= 1
            else:
                break

    return ""


def solve_dfs(words):
    if not words:
        return ""

    trie = Trie()
    for word in words:
        trie.insert(word)

    best_found_word = ""

    def __dfs_rec(node, cur_word):
        nonlocal best_found_word

        if not node.children_lookup:
            return

        for child_char, child_node in node.children_lookup.items():
            if not child_node.is_end:
                continue

            new_word = cur_word + child_char
            if (len(new_word) > len(best_found_word)) or (
                len(new_word) == len(best_found_word) and new_word < best_found_word
            ):
                best_found_word = new_word

            __dfs_rec(child_node, new_word)

    __dfs_rec(trie.root, "")
    return best_found_word


if __name__ == "__main__":
    for fn in (solve, solve_dfs):
        assert fn(["w", "wo", "wor", "worl", "world"]) == "world"
        assert fn(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"
        assert fn(["abc", "bc", "b", "br", "bre", "brea", "break", "breaks"]) == "breaks"
        assert fn([]) == ""
        assert fn(["a"]) == "a"
        assert fn(["b", "wo", "w"]) == "wo"
        assert fn(["b", "ba", "bc"]) == "ba"
        assert fn(["world", "wo", "wor", "worl", "w", "b"]) == "world"
    print("Example tests passed!")

    # Stress test: compare both implementations against an independent
    # brute-force (set-based) checker.
    import random
    import string

    def brute_force(words):
        word_set = set(words)
        best = ""
        for w in words:
            if all(w[:i] in word_set for i in range(1, len(w) + 1)):
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
        return best

    alphabet = string.ascii_lowercase[:4]  # small alphabet to force shared prefixes

    def random_word(max_len=5):
        n = random.randint(1, max_len)
        return "".join(random.choice(alphabet) for _ in range(n))

    for _ in range(1000):
        words = [random_word() for _ in range(random.randint(0, 10))]
        expected = brute_force(words)
        for fn in (solve, solve_dfs):
            actual = fn(words)
            assert actual == expected, (
                f"{fn.__name__} mismatch on words={words}, "
                f"expected={expected}, got={actual}"
            )

    print("All stress tests passed (1000 trials, both implementations)!")
