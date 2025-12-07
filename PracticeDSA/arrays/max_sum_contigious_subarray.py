# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
class Solution:
  # @param A : tuple of integers
  # @return an integer
  def maxSubArray(self, A):

    if not A:
      return 0
    
    max_sum = A[0]
    cur_sum = A[0]
    for i in range(1, len(A)):
      cur_sum = max(A[i], cur_sum + A[i])
      max_sum = max(max_sum, cur_sum)

    return max_sum