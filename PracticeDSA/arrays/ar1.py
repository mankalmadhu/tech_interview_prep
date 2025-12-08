"""
PROBLEM: Array Row Reversal
APPROACH: Two-pointer visualization / Direct math mapping
TIME COMPLEXITY: O(N*M) - We visit every element once.
SPACE COMPLEXITY: O(N*M) - We create a new matrix B of the same size.

CONCEPT:
The goal is to reverse each row of a 2D matrix.
Instead of swapping elements in place (which would be O(1) space but modifies input),
we create a new matrix B.

For every row `i` and column `j`:
The element `A[i][j]` moves to `B[i][n-1-j]`.
This `n-1-j` formula basically says "mirror the index across the center".
"""
def performOps(A):
  m = len(A)
  n = len(A[0])
  B = []
  for i in range(m):
      B.append([0] * n)
      for j in range(len(A[i])):
          B[i][n - 1 - j] = A[i][j]
  return B

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
B = performOps(A)
for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j])
