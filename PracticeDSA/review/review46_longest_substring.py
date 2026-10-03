"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/longest_substring.py until you're done.

Problem (Longest Substring Without Repeating Characters, LeetCode 3):

Given a string s, find the length of the longest substring without
repeating characters.

Example:
  s = "abcabcbb"
  output = 3 (the answer is "abc")

Write your solution below.
"""


def longest_substring(s):
    left  = 0
    lookup = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in lookup:
            lookup.remove(s[left])
            left +=1

        lookup.add(s[right])
        max_len = max(max_len, right-left +1)

    return max_len


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))  # expect 3
    print(longest_substring("bbbbb"))  # expect 1
    print(longest_substring("pwwkew"))  # expect 3
    print(longest_substring(""))  # expect 0

    assert longest_substring("abcabcbb") == 3
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3
    assert longest_substring("") == 0
    assert longest_substring("abba") == 2
    print("fixed cases passed")

    import random
    import string

    def brute_force(s):
        best = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            best = max(best, len(seen))
        return best

    for _ in range(300):
        n = random.randint(0, 15)
        s = "".join(random.choice("ab") for _ in range(n))
        got = longest_substring(s)
        want = brute_force(s)
        assert got == want, f"s={s!r}: expected {want}, got {got}"
    print("300 randomized trials passed")
