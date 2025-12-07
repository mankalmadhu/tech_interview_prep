class Solution:
  # @param A : list of integers
  # @return an integer
  def solve(self, A):
    if not A:
      return 0
    A.sort()
    return A[-1]+ A[0]