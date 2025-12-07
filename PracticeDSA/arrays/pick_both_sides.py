class Solution:
  # https://www.interviewbit.com/problems/pick-from-both-sides/
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def solve(self, A, B):
    max_sum = 0

    if len(A) < B:
      return max_sum
    
    cur_sum = sum(A[0:B])
    max_sum = cur_sum

    for i in range(B):
      cur_sum -= A[B-1-i]
      cur_sum += A[len(A)-1-i]
      max_sum = max(max_sum, cur_sum)

    return max_sum
