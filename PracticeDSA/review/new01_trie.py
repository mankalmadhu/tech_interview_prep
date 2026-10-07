"""
New problem (gap-fill #1/32: Trie) — solve from scratch.

Problem (Implement Trie / Prefix Tree):

Design a trie (prefix tree) data structure that supports:
  - insert(word): inserts the string word into the trie.
  - search(word): returns True if the exact word is in the trie
    (must match a complete inserted word, not just a prefix).
  - starts_with(prefix): returns True if there is any previously
    inserted word that has prefix as a prefix.

Example:
  trie = Trie()
  trie.insert("apple")
  trie.search("apple")      -> True
  trie.search("app")        -> False
  trie.starts_with("app")   -> True
  trie.insert("app")
  trie.search("app")        -> True

Write your solution below.
"""


class TrieNode:
    def __init__(self, is_end):
        self.is_end=is_end
        self.children_lookup={}

    def __repr__(self):
        return f"TrieNode(is_end={self.is_end}, children={list(self.children_lookup.keys())})"


class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word):
        cur_node = self.root
        for i in range(len(word)):
            is_last_char = (True if i== len(word)-1 else False)
            if word[i] in cur_node.children_lookup:
                i_char_node = cur_node.children_lookup[word[i]]
                if is_last_char:
                    i_char_node.is_end = is_last_char
            else:
                i_char_node =  TrieNode(is_last_char)
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

    print("All tests passed!")

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

    for trial in range(300):
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

    print("Stress test passed (300 trials)!")
