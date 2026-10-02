"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/strings/character_replacement.py until you're done.

Problem (Longest Repeating Character Replacement, LeetCode 424):

You are given a string s and an integer k. You can choose any
character of the string and change it to any other uppercase English
character, at most k times.

Return the length of the longest substring containing the same
letter you can get after performing the above operations.

Example:
  s = "ABAB", k = 2   -> 4  (replace the two 'A's or 'B's: "AAAA" or "BBBB")
  s = "AABABBA", k = 1 -> 4  (replace one 'A' in "AABA" -> "AAAA" or
                               one 'B' in "ABBB" style window)

Write your solution below.
"""


def character_replacement(s, k):
    left = 0
    right = 0
    max_len = 0
    char_tracker = {}

    while right < len(s):

        r_char = s[right]
        char_tracker[r_char] = 1 + char_tracker.get(r_char, 0)
        right += 1

        while (right - left - max(char_tracker.values())) > k:
            l_char = s[left]
            char_tracker[l_char] -= 1
            left += 1

        max_len = max((right -left ), max_len)

    return max_len





if __name__ == "__main__":
    fixed_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABCABCBB", 2, 5),
        ("AABCC", 1, 3),
        ("A", 0, 1),
        ("", 2, 0),
    ]
    for s, k, expected in fixed_cases:
        got = character_replacement(s, k)
        assert got == expected, f"{s!r},{k}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random
    from collections import Counter

    def brute_force(s, k):
        n = len(s)
        best = 0
        for i in range(n):
            for j in range(i, n):
                window = s[i:j + 1]
                c = Counter(window)
                maxf = max(c.values())
                if len(window) - maxf <= k:
                    best = max(best, len(window))
        return best

    for _ in range(500):
        n = random.randint(0, 12)
        s = "".join(random.choice("AB") for _ in range(n))
        k = random.randint(0, n)
        got = character_replacement(s, k)
        want = brute_force(s, k)
        assert got == want, f"{s!r},{k}: expected {want}, got {got}"
    print("500 randomized trials passed")
