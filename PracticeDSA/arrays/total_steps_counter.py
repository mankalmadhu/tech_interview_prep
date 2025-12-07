class Solution:
  # @param A : list of integers
  # @param B : list of integers
  # @return an integer
  # https://www.interviewbit.com/problems/steps-by-steps-infinite-grid/

  def coverPoints(self, A, B):
    total_counts = 0
    for i in range(len(A) - 1):
      dx = abs(A[i] - A[i + 1])
      dy = abs(B[i] - B[i + 1])
      total_counts += max(dx, dy)

    return total_counts
