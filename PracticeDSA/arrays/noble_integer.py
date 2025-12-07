#https://www.interviewbit.com/problems/noble-integer/
class Solution:
  # @param A : list of integers
  # @return an integer
  def solve(self, A):

    A.sort()
    count = 0
    n = len(A)
    for i in range(n):
      if i < n - 1 and A[i] == A[i + 1]:
        continue
      if A[i] == n-1-i:
        count += 1
    return count if count > 0 else -1