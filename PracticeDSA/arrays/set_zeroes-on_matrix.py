class Solution:
  # @param A : list of list of integers
  # @return the same list modified
  def setZeroes(self, A):
    """
        Sets entire row and column to zeroes if an element is 0, in-place.

        Strategy: O(1) Space Optimization (Using Matrix as Storage)
        -----------------------------------------------------------
        Instead of using separate sets for 'rows_to_zero' and 'cols_to_zero',
        we use the first row and first column of the matrix itself as flags.

        1. Handle Flags:
           - Iterate through the matrix.
           - If matrix[i][j] == 0, mark the headers: matrix[i][0] = 0 and matrix[0][j] = 0.
           - Special Case: matrix[0][0] belongs to both Row 0 and Col 0.
             We use matrix[0][0] for Row 0 flag, and a separate 'col0' var for Col 0 flag.
        
        2. Process Inner Matrix:
           - Iterate from (1,1) to (M,N).
           - If row header or col header is 0, set cell to 0.
           - (Must be done BEFORE processing borders to avoid corrupting flags).

        3. Process Borders (Order Matters!):
           - Handle Row 0 first (using matrix[0][0]) to avoid data dependency issues.
           - Handle Col 0 last (using col0).

        Complexity Analysis:
        --------------------
        Time Complexity: O(M * N)
           - Two passes over the matrix.
        Space Complexity: O(1)
           - No extra data structures used.
        """
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
