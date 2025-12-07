class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def diffPossible(self, A, B):
    i, j = 0, 1

    if len(A) < 2:
      return 0
    while i < len(A) and j < len(A):
      if i != j and A[j] - A[i] == B:
        return 1
      elif A[j] - A[i] < B:
        j += 1
      else:
        i += 1


if __name__ == "__main__":
  sol = Solution()
  As = [[1, 3, 5], [1, 2, 2, 3, 4]]
  Bs = [4, 0]
  expected = [1, 1]
  for i in range(len(As)):
    assert sol.diffPossible(As[i], Bs[i]) == expected[i]
