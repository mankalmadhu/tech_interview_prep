"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/dp/lcs.py until you're done.

Problem (Longest Common Subsequence, LeetCode 1143):

Given two strings text1 and text2, return the length of their
longest common subsequence. If there is no common subsequence,
return 0.

A subsequence of a string is a new string generated from the
original string with some characters (can be none) deleted without
changing the relative order of the remaining characters.

A common subsequence of two strings is a subsequence that is common
to both strings.

Example:
  text1 = "abcde", text2 = "ace" -> 3 ("ace" is the LCS)
  text1 = "abc", text2 = "abc"   -> 3
  text1 = "abc", text2 = "def"   -> 0

Write your solution below.
"""


def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    memo = [[-1] * (n + 1) for _ in range(m + 1)]
    return lcs_rec(text1, m, text2, n, memo)


def lcs_rec(text1, i1, text2, i2, memo):

    if i1 == 0 or i2 == 0:
        return 0

    if memo[i1][i2] != -1:
        return memo[i1][i2]

    result = 0

    if text1[i1-1] == text2[i2-1]:
        result = 1 + lcs_rec(text1 ,i1-1, text2, i2-1, memo)
    else:
        s1 = lcs_rec(text1, i1-1, text2, i2, memo)
        s2 = lcs_rec(text1, i1, text2, i2-1, memo)
        result = max(s1,s2)

    memo[i1][i2] = result
    return result



def lcs_bottom_up(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else :
                dp[i][j] =  max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]


if __name__ == "__main__":
    cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("abc", "", 0),
    ]
    for t1, t2, expected in cases:
        got = longest_common_subsequence(t1, t2)
        assert got == expected, f"{t1!r},{t2!r}: expected {expected}, got {got}"
    print("fixed cases passed")

    print(lcs_bottom_up("abcde", "ace"))

    import random
    from functools import lru_cache

    def brute_force(text1, text2):
        @lru_cache(maxsize=None)
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if text1[i1] == text2[i2]:
                return 1 + helper(i1 + 1, i2 + 1)
            return max(helper(i1 + 1, i2), helper(i1, i2 + 1))
        return helper(0, 0)

    alphabet = "abc"
    for _ in range(300):
        n1 = random.randint(0, 8)
        n2 = random.randint(0, 8)
        t1 = "".join(random.choice(alphabet) for _ in range(n1))
        t2 = "".join(random.choice(alphabet) for _ in range(n2))
        got = longest_common_subsequence(t1, t2)
        want = brute_force(t1, t2)
        assert got == want, f"{t1!r},{t2!r}: expected {want}, got {got}"
    print("300 randomized trials passed")
