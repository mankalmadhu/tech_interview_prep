def lcs(text1, text2):
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
