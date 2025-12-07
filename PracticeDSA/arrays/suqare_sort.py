class Solution:
  # @param A : list of integers
  # @return a list of integers
  def solve(self, A):
      A_square = [elem*elem for elem in A]
      A_square.sort()
      return A_square
