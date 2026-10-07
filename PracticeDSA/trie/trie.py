# https://leetcode.com/problems/implement-trie-prefix-tree/
"""
Implement Trie (Prefix Tree)

Design a trie (prefix tree) data structure that supports:
  - insert(word): inserts the string word into the trie.
  - search(word): returns True if the exact word is in the trie
    (must match a complete inserted word, not just a prefix).
  - starts_with(prefix): returns True if there is any previously
    inserted word that has prefix as a prefix.

Each TrieNode stores its children in a dict keyed by character (not a
fixed-size array), so it works for any character set, not just
lowercase a-z. Each node also has an `is_end` flag, since "is this a
complete word" can't be inferred from whether a node has children
(e.g. both "app" and "apple" can be inserted, and "app"'s node still
has children for "le" while also being a complete word itself).

Complexity Analysis:
--------------------
Time Complexity: O(L) for insert/search/starts_with, where L is the
   length of the word/prefix - independent of how many words are
   stored.
Space Complexity: O(L) worst case for insert (new nodes created when
   no prefix overlap exists). O(1) extra space for search/starts_with
   (just traversal, no new allocations).
"""


class TrieNode:
    def __init__(self, is_end):
        self.is_end = is_end
        self.children_lookup = {}

    def __repr__(self):
        return (
            f"TrieNode(is_end={self.is_end}, "
            f"children={list(self.children_lookup.keys())})"
        )


class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word):
        cur_node = self.root
        for i in range(len(word)):
            is_last_char = i == len(word) - 1
            if word[i] in cur_node.children_lookup:
                i_char_node = cur_node.children_lookup[word[i]]
                if is_last_char:
                    i_char_node.is_end = True
            else:
                i_char_node = TrieNode(is_last_char)
                cur_node.children_lookup[word[i]] = i_char_node

            cur_node = i_char_node

    def search(self, word):
        cur_node = self.root
        for i in range(len(word)):
            if word[i] in cur_node.children_lookup:
                cur_node = cur_node.children_lookup[word[i]]
            else:
                return False

        return cur_node.is_end

    def starts_with(self, prefix):
        cur_node = self.root
        for i in range(len(prefix)):
            if prefix[i] in cur_node.children_lookup:
                cur_node = cur_node.children_lookup[prefix[i]]
            else:
                return False

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("appl") is False
    assert trie.starts_with("appl") is True
    assert trie.starts_with("b") is False
    assert trie.search("") is False
    assert trie.starts_with("") is True

    # Stress test: compare against independent brute-force (set-based) version
    import random
    import string

    class BruteForceTrie:
        def __init__(self):
            self.words = set()

        def insert(self, word):
            self.words.add(word)

        def search(self, word):
            return word in self.words

        def starts_with(self, prefix):
            return any(w.startswith(prefix) for w in self.words)

    alphabet = string.ascii_lowercase[:4]  # small alphabet to force shared prefixes

    def random_word(max_len=4):
        n = random.randint(1, max_len)
        return "".join(random.choice(alphabet) for _ in range(n))

    for _ in range(300):
        real = Trie()
        brute = BruteForceTrie()
        words = [random_word() for _ in range(random.randint(1, 8))]
        for w in words:
            real.insert(w)
            brute.insert(w)

        for _ in range(20):
            q = random_word()
            assert real.search(q) == brute.search(q), f"search mismatch on {q}, words={words}"
            assert real.starts_with(q) == brute.starts_with(q), (
                f"starts_with mismatch on {q}, words={words}"
            )

    print("All tests passed!")
