
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
