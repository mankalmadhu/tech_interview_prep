class Solution:
  # @param A : integer
  # @param B : integer
  # @param C : integer
  # @param D : integer
  # @return an integer
  def solve(self, A, B, C, D):

    all4equal = (A == B == C == D)
    acbd = (A == C and B == D)
    abcd = (A == B and C == D)
    adbc = (A == D and B == C)

    return 1 if (all4equal or acbd or abcd or adbc) else 0
