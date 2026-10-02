def lcs(text1, text2):
    """
    Finds the length of the Longest Common Subsequence (LCS).

      Difference between Substring vs. Subsequence:
      - Substring: Contiguous characters (e.g., "abc" in "abcde").
      - Subsequence: Characters in relative order but not necessarily contiguous
        (e.g., "ace" in "abcde").

      Strategy: Top-Down Dynamic Programming (Memoization)
      ----------------------------------------------------
      1. State: lcs(m, n) is the LCS length for text1[0...m-1] and text2[0...n-1].
      2. Base Case: If m == 0 or n == 0 (empty strings), LCS is 0.
      3. Recursive Step:
         - Match: If text1[m-1] == text2[n-1]:
           We found a common character! Add 1 and solve for the remainder strings.
           Result = 1 + lcs(m-1, n-1)
         - No Match: If characters differ:
           The LCS might come from skipping the char in text1 OR skipping the char in text2.
           Result = max(lcs(m-1, n), lcs(m, n-1))

      Complexity Analysis:
      --------------------
      Time Complexity: O(M * N)
         - There are M * N unique states (combinations of substring lengths).
         - Each state is computed once due to memoization.

      Space Complexity: O(M * N)
         - For the memoization table of size (M+1) x (N+1).
         - Recursion stack depth is O(M + N).
    """
    m = len(text1)
    n = len(text2)
    memo = [[-1] * (n + 1) for _ in range(m + 1)]
    return lcs_recursive(text1, text2, m, n, memo)


def lcs_recursive(text1, text2, m, n, memo):

    result = 0
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if text1[m - 1] == text2[n - 1]:
        result = 1 + lcs_recursive(text1, text2, m - 1, n - 1, memo)

    else:
        seq_include_text1 = lcs_recursive(text1, text2, m - 1, n, memo)
        seq_include_text2 = lcs_recursive(text1, text2, m, n - 1, memo)
        result = max(seq_include_text1, seq_include_text2)

    memo[m][n] = result

    return result


def lcs_bottom_up(text1, text2):
    """
    Same recurrence as `lcs`, but filled iteratively bottom-up instead of
    via top-down recursion + memoization. Avoids recursion-stack depth
    concerns for long strings.

    Time Complexity: O(M * N). Space Complexity: O(M * N) for the dp table.
    """
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]


if __name__ == "__main__":
    fixed_cases = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("", "abc", 0),
        ("abc", "", 0),
    ]
    for t1, t2, expected in fixed_cases:
        got = lcs(t1, t2)
        assert got == expected, f"{t1!r},{t2!r}: expected {expected}, got {got}"
        got_bu = lcs_bottom_up(t1, t2)
        assert got_bu == expected, f"{t1!r},{t2!r}: expected {expected}, got {got_bu}"
    print("fixed cases passed (both lcs and lcs_bottom_up)")

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
        want = brute_force(t1, t2)
        got = lcs(t1, t2)
        got_bu = lcs_bottom_up(t1, t2)
        assert got == want, f"{t1!r},{t2!r}: expected {want}, got {got}"
        assert got_bu == want, f"{t1!r},{t2!r}: expected {want}, got {got_bu}"
    print("300 randomized trials passed (both lcs and lcs_bottom_up)")
