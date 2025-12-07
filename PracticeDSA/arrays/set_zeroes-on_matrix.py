class Solution:
  # @param A : list of list of integers
  # @return the same list modified
  def setZeroes(self, A):
    rows = set()
    cols = set()
    m = len(A)
    n = len(A[0])
    for i in range(m):
      for j in range(n):
        if A[i][j] == 0:
          rows.add(i)
          cols.add(j)
    for i in range(m):
      for j in range(n):
        if i in rows or j in cols:
          A[i][j] = 0
